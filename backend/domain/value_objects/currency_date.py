from datetime import datetime, date, timedelta
from typing import Self
from domain.value_objects.holidays import BrazilianHolidays

from domain.value_objects.weekdays import WeekDay


class Date:
    day: str = None
    month: str = None
    year: str = None
    _date = None
    is_rest_day: bool = False  # Saturday or Sunday or Holiday

    class InvalidDateException(Exception):
        pass

    class FormatDateException(Exception):
        pass

    def __init__(self, date_as_string: str) -> Self:
        try:
            self._validate_string_date(date_as_string)
            day, month, year = map(int, date_as_string.split("/"))
            self._validate_month(month=month)
            self._validate_day(day=day)
            self._validate_year(year=year)
            self._validate_date(day=day, month=month, year=year)
            self.day = self._format_day(day=day)
            self.month = self._format_month(month=month)
            self.year = self._format_year(year=year)
            self._date = date(year, month, day)
            self.is_rest_day = self.check_if_is_rest_day()
        except self.FormatDateException:
            raise ValueError("Date must be in format dd/mm/yyyy")
        except self.InvalidDateException:
            raise TypeError("Date is not valid")

    def __str__(self) -> str:
        return f"{self.day}/{self.month}/{self.year}"

    def __repr__(self) -> str:
        return self.__str__()

    def __gt__(self, other: "Date") -> bool:
        return self._date > other._date

    def __lt__(self, other: "Date") -> bool:
        return self._date < other._date

    def __ge__(self, other: "Date") -> bool:
        return self._date >= other._date

    def __le__(self, other: "Date") -> bool:
        return self._date <= other._date

    @property
    def day_as_integer(self) -> int:
        return int(self.day)

    @property
    def month_as_integer(self) -> int:
        return int(self.month)

    @property
    def year_as_integer(self) -> int:
        return int(self.year)

    @classmethod
    def _validate_string_date(self, date_as_string: str) -> None:
        if not isinstance(date_as_string, str):
            raise Date.FormatDateException()
        if len(date_as_string.split("/")) != 3:
            raise Date.FormatDateException()

    @classmethod
    def _validate_day(self, day: int) -> None:
        if day < 1 or day > 31:
            raise Date.InvalidDateException()

    @classmethod
    def _validate_month(self, month: int) -> None:
        if month < 1 or month > 12:
            raise Date.InvalidDateException()

    @classmethod
    def _validate_year(self, year: int) -> None:
        if year < 1999 or year > datetime.now().year:
            raise Date.InvalidDateException()

    @classmethod
    def _validate_date(self, day: int, month: int, year: int) -> None:
        try:
            date(year, month, day)
        except ValueError:
            raise Date.InvalidDateException()

    @classmethod
    def _format_day(cls, day: int) -> str:
        return str(day) if day > 9 else f"0{day}"

    @classmethod
    def _format_month(cls, month: int) -> str:
        return str(month) if month > 9 else f"0{month}"

    @classmethod
    def _format_year(cls, year: int) -> str:
        return str(year)

    @staticmethod
    def calculate_correct_working_end_date_by_base_date_and_interval_length(
        base_date: "Date", interval_length_in_days: int
    ) -> "Date":
        """
        This method returns a correct end date by base date and interval length in days
        The end date shouldn't be a rest day
        """
        count = 0
        date_to_check: "Date" = base_date
        while count < interval_length_in_days:
            if not date_to_check.is_rest_day:
                count += 1
                if count == interval_length_in_days:
                    break
                date_to_check = base_date.get_next_date()
            else:
                date_to_check = base_date.get_next_working_date_or_itself()

        return date_to_check

    def __is_weekend(self) -> bool:
        return self._date.weekday() in [WeekDay.SATURDAY.value, WeekDay.SUNDAY.value]

    def __is_holiday(self) -> bool:
        return f"{self.day}/{self.month}" in BrazilianHolidays.__members__.values()

    def get_next_date(self) -> Self:
        current_date = self._date
        next_date = current_date + timedelta(days=1)
        self.__init__(f"{next_date.day}/{next_date.month}/{next_date.year}")
        return self

    def check_if_is_rest_day(self) -> bool:
        return self.__is_weekend() or self.__is_holiday()

    def get_next_working_date_or_itself(self) -> "Date":
        """
        This method returns the next working day
        """
        if not self.is_rest_day:
            return self

        while self.is_rest_day:
            self = self.get_next_date()

        return self
