class StringsCalculator:
    """"
    A simple string calculator to add numbers provided in a string format.
    """

    def add(self, string_numbers):
        """
        add method do sum the numbers given in the input string.

        Parameters:
        string_numbers (str): A string of numbers separated by commas, new lines, or custom delimiters.

        Returns:
        int: sum of the numbers.

        Raises:
        ValueError: If the input string contains negative numbers. The exception message lists all negative numbers.
        """

        if not string_numbers:
            return 0

        if string_numbers.strip() == "":
            return 0

        number_list = self.get_numbers(string_numbers)

        negative_numbers = [str(num) for num in number_list if num < 0]
        if negative_numbers:
            raise ValueError("Negative numbers not allowed: " + ",".join(negative_numbers))

        return sum(number_list)

    def get_numbers(self, string_numbers):
        """
        Extracts numbers from the input string.

        Parameters:
        string_numbers (str): A string of numbers separated by commas, new lines, or custom delimiters.

        Returns:
        list[int]: The list of extracted numbers.
        """

        delimiter = ","
        if string_numbers.startswith("//"):
            delimiter, string_numbers = string_numbers[2:].split("\n", 1)

        string_numbers = string_numbers.replace("\n", delimiter)
        number_list = [int(num) for num in string_numbers.split(delimiter)]

        return number_list