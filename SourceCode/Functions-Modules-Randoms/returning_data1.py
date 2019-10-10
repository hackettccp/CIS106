"""
Demonstrates returning values from functions
"""

def main() :
  #Prompts the user to enter a number. Assigns the user's
  #input (as an int) to a variable named num1
  num1 = int(input("Enter a number: "))

  #Prompts the user to enter another number. Assigns the user's
  #input (as an int) to a variable named num2
  num2 = int(input("Enter another number: "))

  #Passes the num1 and num2 variables as arguments to the printsum
  #function. Assign the value returned to a variable called total
  total = printsum(num1, num2)

  #Prints the value of total
  print("The total is", total)


#A function called printsum that accepts two arguments.
#The function adds the arguments together and returns the result.
def printsum(x, y) :
  #Returns the sum of x and y
  return x + y


#Calls main function
main()

