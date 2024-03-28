"""
The following program returns the factorial of a number.
The factorial of a number is the product of all numbers from 1 to n. For example factorial of
4 represented as 4! is 4x3x2x1 = 24.
Important thing to note is factorial of 0 is also 1.
The program uses the concept of recursive functions to produce the results.
Recursion is a concept that is prevalent in programming languages and is often practised in
programming languages such a C, C++ and Java.
Recursion is the process where a function repeatedly calls itself to perform an operation.
Please refer below:
"""


def factorial(number):
    """
    Calculates the factorial of a number.
    :param number: number whose factorial is to be calculated.
    :return: factorial of the number.
    """
    if number == 0 | number == 1:
        return 1
    else:
        return number * factorial(number - 1)


for i in range(1, 36):
    print(i, factorial(i))
