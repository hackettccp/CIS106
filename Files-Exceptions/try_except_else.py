
"""
Demonstrates using a try...except statement with an else clause.
"""

#Prompts the user to enter a number.
line = input("Enter a number: ")

try:
  #Converts the input to an int.
  number = int(line)

except ValueError:
  #This statement will execute if the input could not be
  #converted to an int (raised a ValueError)
  print("Invalid value")

else:
  #Prints the number the user entered.
  #This statement will only execute if all statements in the
  #try block executed without raising an exception.
  print(number)

#Prints goodbye to show the program has ended.
print("Goodbye!")
