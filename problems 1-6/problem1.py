# ### 1. **Number Guessing Game**:
#    - Write a program that picks a random number between
#      1 and 100, and allows the user to guess the number.
#      The program should tell the user if their guess is
#      too high, too low, or correct. Once the user 
#      guesses correctly, display how many guesses it took.
import random

randomNumber = random.randrange(1,100)

userGuess = int(input("enter a number between 1 and 100:"))

if userGuess == randomNumber :
    print("you got it!")
elif userGuess < randomNumber:
    print("your guess was a little low")
elif userGuess > randomNumber:
    print("your guess was a little high")