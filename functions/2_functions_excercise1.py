"""
Following are the codes to check whether a string is a palindrome. The first function checks
whether a word is a palindrome. The second function checks the same for a sentence.
"""
#   FUNCTION TO CHECK WHETHER A WORD IS A PALINDROME.
print("Please enter the word you want to check for palindrome.")
word = input()


def is_palindrome_word(string):
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()


if is_palindrome_word(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

#   FUNCTION TO CHECK WHETHER A SENTENCE IS A PALINDROME.
"""
The process of checking whether a sentence is a palindrome is a little different from that
of a word. Incase of a sentence all the whitespaces from the string have to be disregarded.
This can be done in 2 ways. We can either use the built in replace() function to simply 
remove the whitespaces. Otherwise we can use a combination of the built in join() and 
split() functions.
"""
print("Please enter the sentence you want to check for palindrome")
sentence = input()
modified_sentence = None
if " " in sentence:
    modified_sentence = sentence.replace(" ", "")
else:
    modified_sentence = sentence
"""
We can replace the code in line 30 with the following as well:
modified_sentence = ''.join(sentence.split(""))
"""


def is_palindrome(string):
    """
    Check if a sentence or word is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.

    :param string: The sentence or word to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()


if is_palindrome(modified_sentence):
    print(f"{sentence} is a palindrome")
else:
    print(f"{sentence} is not a palindrome")

"""
The important concept this excercise covers is the use of docstrings to document the
functions we create. Documentation helps illustrate the use of the functions other users.
Docstrings syntactically should remain within the indentation of the function and there 
should be no line gap between either the function declaration line and the docstring or
the docstring and the function body.
Line 42 to 50 is the docstring for the function is_palindrome().
IDEs like intellij automatically provide the format of the docstring when user enter
three double quotes and enter within the indentation of the function.
The docstring added to the function can be viewed by hovering over the function call
at all instances.
Also, we can view the documentation of the function by placing cursor on the function call
and entering (Ctrl + Q).
The default format of the docstrings offered by the IDE intelliJ can be checked by following
the below mentioned steps:
File -> Settings -> Tools -> Python Integrated Tools -> Docstrings section ->
Docstring format dropdown.
The widely used formats are reStructured Text suggested in Python style Guide PEP8 or
Google suggested by Google.
"""