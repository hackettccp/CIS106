"""
This program simulates the rolling of dice.
"""
#Imports the random module
import random

def main():
    #Create a variable to control the loop.
    again = "y"

    #Simulate rolling the dice.
    while again == "y" or again == "Y":
        print("Rolling the dice...")
        #Gets two random numbers between 1 and 6
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        #Prints the two random numbers
        print("Their values are:")
        print(die1)
        print(die2)
        #Prints the sum of the random numbers
        print("Their total is:")
        print(die1 + die2)

        #Do another roll of the dice?
        again = input("Roll them again? (y = yes): ")

#Calls the main function.
main()
