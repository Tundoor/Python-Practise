# 🐍 Beginner Project: Number Guessing Game
# 🎯 Goal:
# Let the user guess a number between 1 and 100. The program gives hints if the guess is too high or too low until the correct number is guessed.

# what we need:
    
#     1: Generate a random number between 1 and 100.
#    2: Ask the user to guess the number.
#    3: Provide feedback on whether the guess is too high, too low, or correct.

import random

user_input = int(input("Guess A Random Number 1 to 100"))
randomNum = random.randint(0, 100)

if randomNum > user_input:
    print(f"{user_input} was too small. Try Again")

elif randomNum < user_input: 
    print(f"{user_input} is too great. Try Again")
 
else: 
    print("CORRECT!!")

    


# my current dilemna is that it guesses the number but only does it once rather than multiple times with every if statement...
# How I'm thinking of fixing it is creating a function that does the random guessing of the number and allows a person to try over.
# Biggest issue right now... im not sure if python has rules on functions being in a certain scope. 
# Another issue is now it wont have a conditional.