"""
The following piece of code demonstrates that functions can also be used to perform certain
actions rather than just returning values.
The following code prints a multiline string in formatted fashion so that the each line of
string is perfectly centred.
The function we use in the code is supposed to print the following string in a manner that
each line of the string is perfectly centered:
    "Always look on the bright side of life...
    If life seems jolly rotten,
    There's something you've forgotten!
    And that's to laugh and smile and dance and sing,

    When you're feeling in the dumps,
    Don't be silly chumps,
    Just purse your lips and whistle - that's the thing!
    And... always look on the bright side of life..."

The output of the program should resemble the following:
********************************************************************************
**                 Always look on the bright side of life...                  **
**                        If life seems jolly rotten,                         **
**                    There's something you've forgotten!                     **
**             And that's to laugh and smile and dance and sing,              **
**                                                                            **
**                     When you're feeling in the dumps,                      **
**                           Don't be silly chumps,                           **
**            Just purse your lips and whistle - that's the thing!            **
**              And... always look on the bright side of life...              **
********************************************************************************
"""


def text_aligner(text=" ", screen_width=80):
    """
    Print text in console aligned center and bordered by '*'.
    :param text: The text the user wants to be printed aligned
        and bordered
    :param screen_width: Total width of character spaces and
        borders.
    :return: NA
    """
    if len(text) > (screen_width - 4):
        raise ValueError(f"String {text} is larger than the  specified width {screen_width}")
    elif text == "*":
        print('\u001b[35m', "*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print('\u001b[33m', output_string)


"""
In line 33 we assign default values to the arguments during function declaration. these
values will be used instead if the argument values are not passed in the function call.
The syntax in line 35 is used to relay an error in the console to the user with the exact 
details of the issue in order to help with the troubleshooting.
Python allows concrete exceptions which might be thrown in case an error is encountered. It
is also possible for programmers to use these errors under the premonition of a certain
circumstances. The most commonly encountered among these are 'TypeError' and 'ValueError' 
"""

text_aligner("*", 60)
text_aligner("Always look on the bright side of life...", 60)
text_aligner("If life seems jolly rotten,", 60)
text_aligner("There's something you've forgotten!", 60)
text_aligner("And that's to laugh and smile and dance and sing,", 60)
text_aligner(screen_width=60)
text_aligner("When you're feeling in the dumps,", 60)
text_aligner("Don't be silly chumps,", 60)
text_aligner("Just purse your lips and whistle - that's the thing!", 60)
text_aligner("And... always look on the bright side of life...", 60)
text_aligner("*", 60)

"""
In the above code  fragment we make function calls mutliple times. It is important to note
that during each of these function calls we are passing the value of the screen_width
argument as 60 (Even thought the default value that we have set during function declaration
is 80.
Also, in line 58 we are making a call without passing the first parameter. Instead of just
passing the value for screen_width we are mentioning the argument for which the value is
being passed.
The concept used in line 58 is referred to as keyword arguments.  Keyword arguments are a
way to pass values to a function by explicitly specifying the parameter names along with 
their corresponding values. This provides clarity and flexibility, especially when dealing
with functions that have a large number of parameters.
"""