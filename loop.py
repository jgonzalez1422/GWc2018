#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)
i = 8

Try = 0


guess = input("Guess a number between 1 and 20 (inclusive): ")
if not guess.isnumeric(): # checks if a string is only digits 0 to 9
	print("That's not a positive whole number, try again!")
else:
	guess = int(guess) # converts a string to an integer

    print("I am thinking of a number between 1 and 20")
    while i < 6:
        print("Take a guess")
        guess = input()
        guess= int(guess)

        i += 1

        if guess < 9:
            print("Your guess is too high")

        if guess > 7:
            print("Your guess is too low ")

        if guess == i:
            print("Correct!")
            break



	guess = int(guess) # converts a string to an integer
