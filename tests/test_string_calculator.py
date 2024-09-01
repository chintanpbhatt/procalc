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


def test_add_any_amount_of_numbers(calculator):
    assert calculator.add("5,10,15") == 30


def test_add_any_amount_of_numbers_with_new_lines(calculator):
    assert calculator.add("5\n10,15") == 30


@pytest.mark.parametrize(
    "numbers, expected_sum",
    [("//;\n1;2", 3), ("//|\n1|2|3", 6), ("//#\n1#2#3#4", 10)],
)
def test_add_any_amount_of_numbers_custom_delimiter(calculator, numbers, expected_sum):
    assert calculator.add(numbers) == expected_sum
