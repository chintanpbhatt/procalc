from app.string_calculator import StringCalculator


def test_add_empty_string():
    calculator = StringCalculator()
    assert calculator.add("") == 0
