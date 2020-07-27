"""
Demonstrates prompting a user to enter input using
the keyboard.

This demonstrates two different ways to get the user's input
as a string and converts the input to an int-type.
The same thing can be done for floats by using the float function
instead of the int function.
"""

#Gets the user's first number.
#The input function will print "Enter the first number: " and
#wait for the user to type their entry.
#When the user presses the "Enter" key on their keyboard,
#the value they typed will be returned and assigned to the
#number1 variable.
number1 = input("Enter the first number: ")
#The number1 variable is converted from a string to an int, and
#is assigned back to itself. This replaces the string-type value of
#the number1 variable with the int-type value.
number1 = int(number1)

#Gets the user's second number.
#The input function will print "Enter the second number: " and
#wait for the user to type their entry.
#When the user presses the "Enter" key on their keyboard,
#the value they typed will be returned (as a string-type) and
#immediately passed to the int function. The int-type value returned
#from the int function will be assigned to the number2 variable.
number2 = int(input("Enter the second number: "))

#Prints the sum of the two numbers.
print("The sum of the two numbers is", number1 + number2)
