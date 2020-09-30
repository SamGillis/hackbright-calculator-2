"""Functions for common math operations."""


def add(numbers):
    """Return the sum of the two input integers."""
    
    total = 0
    for number in numbers:
        total = total + number
        
    return total


def subtract(numbers):
    """Return the second number subtracted from the first."""

    total = numbers[0]
    for number in numbers[1:]:
        total = total - number
    return total


def multiply(numbers):

    """Multiply the two inputs together."""
    total = 1
    for number in numbers:
        total = total * number
    return total


def divide(numbers):
    """Divide the first input by the second and return the result."""

    total = numbers[0]
    for number in numbers[1:]:
        total = total / number
    return total


def square(numbers):
    """Return the square of the input."""

    squares = []
    for number in numbers:
        squares.append(number ** 2)
    
    return squares


def cube(numbers):
    """Return the cube of the input."""

    cubed_nums = []
    for number in numbers:
        cubed_nums.append(number ** 3)
    return cubed_nums


def power(numbers):
    """Raise num1 to the power of num2 and return the value."""

    total = numbers[0]
    for number in numbers[1:]:
        total = total ** number
    return total  # ** = exponent operator


def mod(numbers):
    """Return the remainder of num1 / num2."""

    return numbers[0] % numbers[1]
