import re


class StringCalculator:
    DELIMITER_INDICATOR = '//'

    def add(self, numbers: str):
        if not numbers:
            return 0

        delimiter = ',|\n'

        if numbers.startswith(StringCalculator.DELIMITER_INDICATOR):
            parts = numbers.split('\n', maxsplit=1)
            delimiter = parts[0][len(StringCalculator.DELIMITER_INDICATOR) :]
            delimiter = re.escape(delimiter)
            numbers = parts[1]
        numbers_str_list = re.split(delimiter, numbers)
        numbers_list = [float(string) for string in numbers_str_list]
        return int(sum(numbers_list))
