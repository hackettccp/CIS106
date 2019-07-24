"""
Demonstrates global variables.
"""

def main():
    #Creates a global variable named number within the main function.
    global number
    #Prompts the user to enter a number. The user's input is converted to
    #an int-type and assigned to the global variable, number
    number = int(input("Enter a number: "))
    #Calls the shownumber function
    shownumber()

#Function that simply prints the value of the global variable, number
def shownumber():
    print("The number you entered is", number)

#Calls the main function.
main()

