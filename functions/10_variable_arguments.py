"""
In Python, *args is a special syntax in a function definition that allows you to pass a
variable number of positional arguments to the function. The *args syntax allows a function to
accept any number of positional arguments, which are then gathered into a tuple.
Generally the prefix '*' is used to unpack a sequence. Hence, when we are passing *args as a
function parameter, it accepts any number of values during function call and wraps them into a
tuple. Please refer to the below example:
"""
import colorama


def test_star(*args):
    print(*args)
    print(args)
    for x in args:
        print(x)


test_star(1, 2, 3, "four", 5.0)

"""
The above code will produce the following output:
1 2 3 four 5.0
(1, 2, 3, 'four', 5.0)
1
2
3
four
5.0

The code in line 12 prints the unpacked tuple. Hence, it is represented in the output 
without the parenthesis. It is important to note that since, *args represents an unpacked tuple
, it mean args represents the tuple. Hence, the code in line 13 prints the tuple . The code in 
lines 13 and 14 prints the individual values from the unpacked tuple.
Let us further exploit this feature by reusing the colour printing feature of python as 
illustrated in the excercise 5.
The program in excercise 5 was limited in its means since it only allowed one effect to be 
applied on the text at a time. However, using *args we can further optimize the program to 
be able to apply more than the one effects on the text. Please refer below.
"""

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def print_effect(text: str, *effects: str) -> None:
    """
    Print text using ANSI sequences to change colour, effects etc. If no effects are
    mentioned, then the text is printed in default terminal colour.
    :param text: The text to be printed.
    :param effects: The colours or effects that we want to apply on the text based on the
        constants mentioned at the start of the file.
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


colorama.init()
print_effect("Hello Red", RED)
print_effect("Hello Red in bold", RED, BOLD)
print_effect("Hello Blue", BLUE)
print_effect("Hello Green in reverse", GREEN, REVERSE)
print_effect("Hello Cyan", CYAN)
print_effect("Hello Magenta bold and underline", MAGENTA, BOLD, UNDERLINE)
print_effect("Hello White", WHITE)
colorama.deinit()

"""
For all the effects to be applied to the text, the function code in line 65 joins the values in
the 'effects' tuple and forms an effect string which is then passed into the output string.
Hence, we are able to pass multiple parameter values only through a single variable name.

It is important to note few rules for variable positional arguments in functions:
1.  Variable positional arguments cannot have default values.
2.  When function has more than one type of arguments i.e standard arguments, variable 
    positional arguments, keyword arguments and variable keyword arguments, the order of the 
    arguments in the function definition should be as follows:
    i. standard arguments
    ii. variable positional arguments
    iii. keyword arguments
    iv. variable keyword arguments
    This order is a convention and not a strict rule, but following it is recommended for 
    clarity and consistency. 
    Please refer to the below function declaration:
    def func(*args, x, y)
    In the above case the interpreter will not be able to figure out where the parameter 
    values for *args ends and values for x and y begin during a function call. Hence, the ideal
    way to define the above function would be: def func(x, y, *args)
"""
