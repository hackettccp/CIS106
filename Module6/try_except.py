
"""
Demonstrates a try...except statement
"""

#Prompts the user to enter a number.
line = input("Enter a number: ")

try:
  #Converts the input to an int.
  number = int(line)
  #Prints the number the user entered.
  print(number)

except ValueError:
  #This statement will execute if the input could not be
  #converted to an int (raised a ValueError)
  print("Invalid value")

#Prints goodbye to show the program has ended.
print("Goodbye!")
