from enum import Enum


class WeekDay(Enum):
    """
    This enum follows the Python weekday convention from built-in datetime module
    Where Monday is 0 and Sunday is 6
    """

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
