from typing import Self


class Rate:
    value = None

    class InvalidRateException(Exception):
        pass

    class InvalidRateValueException(Exception):
        pass

    @classmethod
    def _validate_rate_type(self, rate_value: float) -> None:
        if not isinstance(rate_value, float):
            raise Rate.InvalidRateException()

    @classmethod
    def _validate_rate_value(self, rate_value: float) -> None:
        if rate_value < 0:
            raise Rate.InvalidRateValueException()

    @classmethod
    def _round_rate_value(self, rate_value: float) -> float:
        return round(rate_value, 3)

    def __init__(self, rate_value: float) -> Self:
        try:
            self._validate_rate_type(rate_value=rate_value)
            self._validate_rate_value(rate_value=rate_value)
            self.value = self._round_rate_value(rate_value=rate_value)
        except self.InvalidRateException:
            raise TypeError("Rate must be a float")
        except self.InvalidRateValueException:
            raise ValueError("Rate must be greater than 0")
