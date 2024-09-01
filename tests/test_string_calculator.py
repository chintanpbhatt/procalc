import pytest
from app.string_calculator import StringCalculator


@pytest.fixture
def calculator():
    return StringCalculator()


def test_add_empty_string(calculator):
    assert calculator.add("") == 0


@pytest.mark.parametrize(
    "numbers, expected_sum",
    [
        ("5", 5),
        ("10", 10),
    ],
)
def test_add_single_number(calculator, numbers, expected_sum):
    assert calculator.add(numbers) == expected_sum


def test_add_two_numbers(calculator):
    assert calculator.add("1,2") == 3
