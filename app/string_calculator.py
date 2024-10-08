import re

# if * then muliplity


class StringCalculator:
    DELIMITER_INDICATOR = '//'

    def parse_numbers(func):

        def wrapper(*args, **kwargs):
            numbers = args[1]
            delimiter = ',|\n'
            if numbers.startswith(StringCalculator.DELIMITER_INDICATOR):
                parts = numbers.split('\n', maxsplit=1)
                delimiter_section = parts[0][len(StringCalculator.DELIMITER_INDICATOR) :]
                if delimiter_section.startswith('[') and delimiter_section.endswith(']'):
                    # Handling multiple delimiters enclosed in square brackets
                    delimiters = re.findall(r'\[(.*?)\]', delimiter_section)
                    delimiter = '|'.join(re.escape(delim) for delim in delimiters)
                else:
                    delimiter = re.escape(delimiter_section)

                numbers = parts[1]

            numbers_str_list = re.split(delimiter, numbers)
            m_args = list(args)
            m_args[1] = numbers_str_list

            my_keys = {}
            my_keys['is_muliply'] = False
            if delimiter == re.escape('*'):  # '\*':
                my_keys['is_muliply'] = True
            return func(*m_args, **my_keys)

        return wrapper

    @parse_numbers
    def add(self, numbers: list[str] | str, is_muliply=False):
        print(is_muliply)
        if not numbers:
            return 0

        total = 0
        negatives = []

        for num in numbers:
            if num:
                n = float(num)
                if n > 1000:
                    continue
                if n < 0:
                    negatives.append(int(n))
                if is_muliply:
                    if total == 0:
                        total = 1
                    total *= n
                else:
                    total += n

        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

        return int(total)
