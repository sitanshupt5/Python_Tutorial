"""
The following program prints the fibonacci series.
The Fibonacci series is a sequence of numbers where each number is the sum of the two
preceding ones, usually starting with 0 and 1. In mathematical terms, it is defined by
the recurrence relation:
F(n)=F(n−1)+F(n−2)

with initial conditions:
F(0)=0,F(1)=1
So, the Fibonacci sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
Following program prints the fibonacci sequence upto the nth number in the sequence.
"""


def fibonacci(n):
    """
    Return the 'n'th fibonacci number for positive 'n'.
    :param n: The occurence of the number in the sequence.
    :return: list of fibonacci numbers upto the nth number.
    """
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series


result = fibonacci(10)
print(result)


# The same program can be written in a different way without using lists:


def fibonacci_2(n):
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result


for i in range(36):
    print(i, fibonacci_2(i))