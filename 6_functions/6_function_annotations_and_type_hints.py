"""
Function annotations in Python provide a way to attach metadata or additional information
to the parameters and return value of a function. Annotations do not affect the runtime
behavior of the code; they are simply used for documentation purposes or for tools that
might analyze the code.
Please refer to the following example:
"""
from typing import List, Optional


def addition(x: int, y: int) -> int:
    """
    Adds two numbers and returns the result.
    :param x: The first number.
    :param y: The second number
    :return: The sum of first and second numbers
    """
    return x + y


result = addition(5, 3)
print(result)
"""
In the above example:
1. x: int and y: int are function parameter annotations that x and y are expected to be of
    type int.
2. -> int is the return type annotation, specifying that the function returns an integer.

These annotations are optional and do not enforce type checking. They are mainly used for
documentation and to provide hints to tools that support type checking.

Type hints in Python provide a way to indicate the expected types of variables, function 
parameters, and return values. While Python is a dynamically-typed language, meaning you 
don't explicitly declare the data type of a variable, type hints allow you to add optional
type information to your code. This can be useful for documentation, code readability, and
for tools that perform static type checking.
Providing type hints for basic data types in python (i.e int, float, bool, str etc) is 
fairly easily using annotations. However, providing annotations for complex data types
can be tricky.
This achieved by importing the typing module in python. Please refer to the below example:
"""


def fibonacci(n: int) -> List[int]:
    """
    Return the `n` th fibonacci number for positive `n`.
    :param n: The occurence of the number in the sequence.
    :return: list of fibonacci numbers upto the nth number.
    """
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series


result = fibonacci(10)
print(result)

"""
In the above example in order to provide the type hint for the return value of the function
we had to import List from the typing module.
Similarly, we can use 'Any' if we want to allow any type of data.
We can also use 'Optional'. Please refer to the below example:
"""


def multiplication(x: float, y: Optional[float]) -> Optional[float]:
    return x * y


print(multiplication(5, 5))

"""
Here, Optional[float] indicates that y can be either float or None.

We can also provide type hints for the function parameters that have default values.
In such a case the the assignment operator has to be surrounded by spaces (' ').
Please refer to the following example:
"""


def subtraction(x: int = 10, y: int = 5):
    return x - y


print(subtraction(15, ))