"""
Demonstrates parameters and arguments
"""

def main() :
  #Prompt the user to enter a number. Assign the user's
  #input (as an int) to a variable named num1
  num1 = int(input("Enter a number: "))

  #Prompt the user to enter another number. Assign the user's
  #input (as an int) to a variable named num2
  num2 = int(input("Enter another number: "))

  #Pass the num1 and num2 variables as arguments to the printsum
  #function
  printsum(num1, num2)


#A function called printsum that accepts two arguments.
#The function sums the arguments and prints the result.
def printsum(x, y) :
  #Prints the sum of x and y
  print("The sum of the numbers is", x + y)


#Calls main function
main()

