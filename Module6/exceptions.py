
"""
Demonstrates different exception handling examples
"""

#This function accepts an argument that the function divides by
#100. It returns the result of that division.
def divide100(valueIn) :
  if valueIn < 0 :
    #Raises an exception if the argument was negative.
    raise Exception("Negative number supplied to divide100 function.")
  else:
    return 100 / valueIn

#Prompts the user to enter a number.
line = input("Enter a number: ")

#This loop continues as long as the user did not
#type "exit" as their input.
while line.lower() != "exit" :
  try :
    #Calls the divide100 function, passing the user's input as
    #an argument.
    result = divide100(int(line))
  except ValueError :
    #This statement will execute if the input could not be
    #converted to an int (raised a ValueError)
    print("Invalid input.")
  except ZeroDivisionError :
    #This statement will execute if the user's input was zero.
    #A ZeroDivisionError would have been raised by the division
    #operation in the divide100 function.
    print("Cannot divide by zero.")
  except :
    #This statement will execute if any other type of exception occurred.
    #The custom exception raised in the divide100 function will be
    #handled here.
    print("Error. Reason: " + str(error))
  else :
    #Prints the result of the division
    print(result)
  finally :
    #Prompts the user to enter new input.
    #This statement is executed regardless of if an exception occurred
    #in the try block.
    line = input("Enter a number: ")

#Prints goodbye to show the program has ended.
print("Goodbye!")
