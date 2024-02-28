"""
Following program is for a guessing game. The system chooses a random number between a
certain range. The users job is to guess the number. The system is supposed to direct the
user to guess the correct number. For example if the number is lower than the guess then
the system should direct the user to guess lower and likewise if higher.
If the user enters '0' as the input then the program exits. If the user enters an invalid
number then the program directs the user to enter a numeric instead and waits for another
input.
"""
import random

highest = 1000
answer = random.randint(1, highest)
print(answer)
guess = 0
print(f"Please guess number between 1 and {highest}")


def get_integer(prompt):    # function to gather input from the user.
    """
    Get and integer from Standard Input(stdin)

    The function will continue looping and prompting
    the user until a valid 'int' is entered.

    :param prompt: The string that the user will see, when
        prompted to enter the value
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)    # making sure the value returned in the form of an integer
        else:
            print(f"{temp} is not valid number")


while guess != answer:
    guess = get_integer(": ")
    if guess == 0:      # Exit condition
        break
    elif guess == answer:
        print("Well done you have guess it!!!")
        break
    else:               # When guess is not equal to the answer
        if guess > answer:
            print("Please guess lower.")
        else:
            print("Please guess higher.")