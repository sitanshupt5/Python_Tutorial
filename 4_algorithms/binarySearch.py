"""
Binary search is a divide-and-conquer algorithm that allows you to search for a specific
value within a sorted array (or list) by repeatedly dividing the search interval in half.
Imagine we have a number say '8' in mind. The computer has to pin point that number from
a range of 100 numbers. In order to reduce the search length the computer has to reduce
the search length by reducing the number of comparisons. This can be achieved by letting
the computer know whether the concerned number is higher or lower than the guess.
The computer starts by comparing the number to the half of the range, i.e. 50. As the
number is lower then the computer searches within the range of 1 to 49 and the integer
half of that is 25. Since, the number is still lower than the guess, the computer will
now check within the range of 1 to 24 and compare the number with 12. Again, since number
is lower than the guess, the computer searches within the interval of 1 to 11 and compare
the number with 6. This time the number is higher than the guess. Hence, the computer
searches within the interval of 7 and 11 and compares the number with 9. Again the number
is lower than 9. So the range now becomes 7 to 8 and comparison happens with 7. Finally
due to the mismatch the only remaining option is 8. Hence, a match. Here instead of
8 comparisons the number was guessed within 7.
In binary search the if the range is 1 to 2^n , then the computer can guess the number
within a maximum of n guesses. Hence, if the range is 1 to 1024, then the computer can
find the number with a maximum of 10 comparisons.
Following is the example of how binary search works.
"""
import random

lowerLimit = 1
upperLimit = 1000
answer = random.randint(lowerLimit, upperLimit)
guess = 0
guesses = 1
while guess != answer:
    print("\tGuessing in the range of {} and {}".format(lowerLimit, upperLimit))
    guess = lowerLimit + (upperLimit - lowerLimit)//2

    if guess > answer:
        upperLimit = guess -1
    elif guess < answer:
        lowerLimit = guess +1
    else:
        print("Guessed it!! The answer is {}".format(guess))
        print("It took {} guesses".format(guesses))
        break
    guesses +=1


"""
We are writing a program where we have to think of a random number between 1 and 1000.
The number will be guessed by the computer. If the
guess is lower than our number then we should notify computer in the console to guess
lower. Similarly, if number is higher than the guess then we should notify computer in the
console to guess higher. If the guess is correct then we notify the computer in the console
and in return the computer displays the number of guesses it took in the console.
"""
high = 100
low = 1

print("Please think of a number between {} and {}". format(low, high))
input("Press enter to start")

guesses = 1
while True:
    print("\tGuessing in the range of {} and {}".format(low, high))
    guess = low+(high-low)//2
    response = input("My guess is {}. Should i guess higher or lower?"
                     "Enter h for higher and l for lower. If my guess is correct enter c"
                     .format(guess))
    if response == "h":
        # Guess higher. So low value should be guess + 1.
        low = guess + 1
    elif response == "l":
        # Guess lower. So high value should be guess -1.
        high = guess - 1
    elif response == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")
    guesses = guesses + 1