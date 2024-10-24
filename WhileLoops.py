### Part Two -- your code goes here. 
import random
numberToGuess = random.randint(1, 100)
# uncomment below to make testing easier
# print(f"Number is {numberToGuess}")
notGuessed = True
while notGuessed:
    userInput = int(input("guess a number between 1 and 100: "))
    if userInput == numberToGuess:
        notGuessed = False
print("Correct guess")