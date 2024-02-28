"""
We can colour code the output that we print on the console using certain escape characters.
It is also possible to  add effects to the output printed on the console such as bold,reverse
or underline.
Please refer to the below program code for reference:
"""
import colorama

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

print("Hi this is Sitanshu.")

"""
Normally the above line of code will be printed in the console with the default colour of 
the IDE (white in my case). But tweaking the code slightly as in the below example will 
change the colour of the output on the console to our choice.
"""

print(BLUE, "Hi this is Sitanshu.")
print("Subhransu is my best friend")

"""
However, this may raise another problem. After use the colour doesn't go back to default.
i.e For all the subsequent print operations the colour of output remain BLUE. This can be 
resolved using the escape characters for RESET.
Let us create a function that prints the output based on our choice of effect.
"""


def print_effect(text: str, effect: str = WHITE) -> None:
    """
    Print text using ANSI sequences to change colour, effects etc. If no effects are
    mentioned, then the text is printed in default terminal colour.
    :param text: The text to be printed.
    :param effect: The colour or effect that we want to apply on the text based on the
        constants mentioned at the start of the file.
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


print_effect("Hi this is Sitanshu", UNDERLINE)
print_effect("Subhransu is my best friend")

"""
Although producing output text in different colors or effects is easily achieved in an IDE like
IntelliJ or Pycharm using ANSI escape code, there is still an issue of reproducing these in 
the terminal windows or linux.
Colorama is a python package that provides such cross platform for adding colored output to 
terminal text.The primary purpose of Colorama is to make it easy to produce colored text in 
terminal environments, which often have limited support for text formatting. Colorama works on 
both Windows and Unix-like systems, making it a convenient choice for developers who need 
consistent colored output across different platforms. In order to test that we need to 
download that colorama .whl file and add the package. Only then can we import the package to our
module and use it.
We have already imported the colorama package to our module. Lets use and see how it works.
"""

colorama.init()
print_effect("Hello Red", RED)
print_effect("Hello Blue", BLUE)
print_effect("Hello Green", GREEN)
print_effect("Hello Cyan", CYAN)
print_effect("Hello Magenta", MAGENTA)
print_effect("Hello White", WHITE)
colorama.deinit()


