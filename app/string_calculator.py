class StringCalculator:
    def add(self, numbers: str):
        if not numbers:
            return 0

        if ',' in numbers:
            numbers_str_list = numbers.split(',')
            numbers_list = [float(string) for string in numbers_str_list]
            return int(sum(numbers_list))

        if len(numbers) >= 1:
            return int(numbers)
