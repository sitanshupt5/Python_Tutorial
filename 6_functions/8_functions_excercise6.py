"""
The following shows a guessing game where the program guesses a number. The algorithm actually
replicates that of a binary search. However, in this program we will achieve it with the help
of functions.
"""
LOW = 1
HIGH = 1000


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        guess = low + ((high - low) // 2)
        if guess < answer:
            low = guess + 1
        elif guess > answer:
            high = guess - 1
        elif guess == answer:
            return guesses
        guesses += 1


for number in range(LOW, HIGH +1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print(f"{number} guessed in {number_of_guesses}")

"""
The above function returns the minimum number of guesses it will take the computer to guess 
a number correctly between 1 and 1000.
"""