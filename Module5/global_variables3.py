"""
Demonstrates global variables
"""

#Declares a variable named g_variable and assigns it
#the value "I'm a global variable"
g_variable = "I'm a global variable"

def main() :
  #Prints the value of g_variable
  print(g_variable)
  
  #Calls the localtest function
  localtest()

  #Attempts to print the value of the local_var variable
  #It is unable to, because local_var exists only in the
  #localtest function.
  #To fix, comment out or remove the below line
  print(local_var)


#A function called localtest
def localtest() :
  #Prints the text "In local_test function"
  print("In local_test function")
  
  #Prints the value of g_variable
  print(g_variable)

  #Declares a variable named local_var and assigns it
  #the value "I'm a local variable"
  local_var = "I'm a local variable"

  #Prints the value of local_var
  print(local_var)


#Calls main function
main()

