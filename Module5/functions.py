"""
Demonstrates functions
"""

def main() :
  #Calls the hello function
  hello()

  #Calls the printsum function
  printsum() 

#A function called hello that prints a line of output
def hello() :
  #Print the text "Hello World!"
  print("Hello World!")

#A function called printsum that prompts the user to enter
#two numbers and prints the sum of the two numbers.
def printsum() :
  #Prompts the user to enter a number. Assigns the user's
  #input (as an int) to a variable named num1
  num1 = int(input("Enter a number: "))

  #Prompts the user to enter another number. Assigns the user's
  #input (as an int) to a variable named num2
  num2 = int(input("Enter another number: "))

  #Prints the sum of num1 and num2
  print(num1 + num2)

#Calls main function
main()



