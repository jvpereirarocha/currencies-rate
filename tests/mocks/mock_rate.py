from pytest import fixture

from domain.value_objects.rate import Rate


@fixture(scope="function")
def mock_rate():
    def _create_mock(rate_value: float = 1.0) -> Rate:
        return Rate(rate_value)

    return _create_mock
