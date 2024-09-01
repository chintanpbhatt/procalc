import pytest
from app.string_calculator import StringCalculator


def test_add_empty_string():
    calculator = StringCalculator()
    assert calculator.add("") == 0


@pytest.mark.parametrize(
    "numbers, expected_sum",
    [
        ("5", 5),
        ("10", 10),
    ],
)
def test_add_single_number(numbers, expected_sum):
    calculator = StringCalculator()
    assert calculator.add(numbers) == expected_sum
