#!/usr/bin/env python3

"""This module contains useful functions to perform mathematical operations and
return the results for use in the API response."""

import math


def is_even(number: int) -> bool:
    """Return true if `number` is even, else false.

    Args:
        number(int): The number to check

    Return:
        bool: True | False based on the outcome
    """
    return number & 1 == 0


def is_perfect(number: int) -> bool:
    """Return true if a `number` is perfect or not.

    Args:
        numbe(int): The number to check

    Return:
        bool: True | False based on the outcome.
    """
    if not is_even(number):
        return False  # it's unknown whether there are any odd perfect numbers

    return __is_perfect(number)


def __is_perfect(number: int) -> bool:
    """A helper for the `is_perfect()` function.

    Return:
        bool: True if the `number` is perfect, False otherwise.
    """
    total = 1

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:  # it's a divisor if it divides completely
            total += divisor + number / divisor
        divisor += 1

    return total == number


def digit_sum(number: int) -> int:
    """Returns the digit sum of the provided `number`.

    The digit sum of a number is the sum of of all its digits.

    Args:
        number(int): The number the to get its digit sum.
    """
    number_sum = 0

    while number != 0:
        last = number % 10

        number_sum += last
        number //= 10

    return number_sum


def is_prime(number: int) -> bool:
    """Return True if `number` is a prime number, False otherwise."""
    if number <= 1:
        return False

    if number == 2 or number == 3:
        return True

    if is_even(number) or number % 3 == 0:
        return False

    divisor = 5

    while divisor <= math.sqrt(number):
        if number % divisor == 0 or number % (divisor + 2) == 0:
            return False

        divisor += 6  # move to the next prime number

    return True


def is_armstrong(number: int) -> bool:
    """Return True if `number` is an Armstrong number, False otherwise."""
    number_sum = 0
    number_len = len(str(number))

    temp_num = number

    while temp_num != 0:
        last = temp_num % 10
        number_sum += last**number_len
        temp_num //= 10

    return number_sum == number


def build_number_properties(number: int) -> list[str]:
    """Builds the properties of a number.

    The properties included are whether it and `odd`, `even` or `armstrong`.
    The results are stored in a list of strings.

    Args:
        number(int): The number to build properties for.

    Return:
        list[str]: The properties of the number. E.g., `["odd", "armstrong"]`
    """
    properties: list[str] = []

    if is_even(number):
        properties.append("even")
    else:
        properties.append("odd")

    if is_armstrong(number):
        properties.append("armstrong")

    return properties
