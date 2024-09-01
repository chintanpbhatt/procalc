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

        total = 0
        negatives = []

        for num in numbers_str_list:
            if num:
                n = float(num)
                if n < 0:
                    negatives.append(int(n))
                total += n

        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

        return int(total)
