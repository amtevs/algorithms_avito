import pytest
from palindrom import palindrom


@pytest.mark.parametrize(
    "value,expected",
    [
        (0, True),
        (1, True),

        (11, True),
        (22, True),
        (12, False),
        (21, False),

        (101, True),
        (121, True),
        (123, False),
        (321, False),

        (1001, True),
        (1221, True),
        (1234, False),
        (4321, False),

        (10001, True),
        (12321, True),
        (12345, False),

        (123321, True),
        (123456, False),
        (123454321, True),
        (123456789, False),
    ],
)
def test_palindrom_basic(value, expected):
    assert palindrom(value) == expected