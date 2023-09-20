from domain.value_objects.currency_date import Date


class IntervalOfDates:
    class InvalidInterval(Exception):
        pass

    def __init__(self, start_date: Date, end_date: Date):
        self._validate_interval(start_date=start_date, end_date=end_date)
        self.start_date = start_date
        self.end_date = end_date

    def _validate_interval(self, start_date: Date, end_date: Date) -> None:
        if start_date > end_date:
            raise IntervalOfDates.InvalidInterval()

    def __str__(self) -> str:
        return f"{self.start_date} - {self.end_date}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: "IntervalOfDates") -> bool:
        return self.start_date == other.start_date and self.end_date == other.end_date

    @classmethod
    def date_is_in_the_interval(
        cls, date_to_compare: Date, interval: "IntervalOfDates"
    ) -> bool:
        return interval.start_date <= date_to_compare <= interval.end_date

    def interval_of_dates_is_valid(self, interval_length_in_days: int) -> bool:
        """
        This interval is valid only if:
        - the end date is greather than equals to the number of interval_length_in_days passed as parameter
        """
        correct_working_interval = (
            self.get_correct_working_start_end_date_by_interval_length(
                interval_length_in_days=interval_length_in_days
            )
        )

        interval_is_valid: bool = True

        if self.end_date > correct_working_interval.end_date:
            interval_is_valid = False

        return interval_is_valid

    def get_correct_working_start_end_date_by_interval_length(
        self, interval_length_in_days: int
    ) -> "IntervalOfDates":
        """
        This method returns a correct interval of dates by start and end date
        The interval has the number of days specified in interval_length_in_days
        The start date is the same but the end date shouldn't be a rest day
        """

        correct_end_working_date = (
            Date.calculate_correct_working_end_date_by_base_date_and_interval_length(
                base_date=self.start_date,
                interval_length_in_days=interval_length_in_days,
            )
        )

        return IntervalOfDates(
            start_date=self.start_date, end_date=correct_end_working_date
        )
