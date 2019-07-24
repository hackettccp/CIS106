"""
Demonstrates using a module
"""
#Import the moduletools module
import moduletools

def main() :
  #Prompts the user to enter a length, width and height
  #Stores each input (as an int) to variables named length, width
  #and height
  length = int(input("Enter a length: "))
  width = int(input("Enter a width: "))
  height = int(input("Enter a height: "))

  #Passes the length, width and height variables as arguments to the
  #moduletools' getsurfacearea function. Assigns the value returned to
  #a variable named surface_area
  surface_area = moduletools.getsurfacearea(length, width, height)

  #Passes the length, width and height variables as arguments to the
  #moduletools' getvolume function. Assigns the value returned to
  #a variable named volume
  volume = moduletools.getvolume(length, width, height)

  #Prints the values of the surface_area and volume variables
  print("The surface area is", surface_area)
  print("The volume is ", volume)

  #Passes the length, width and height variables as arguments to the
  #moduletools' iscube function. Based on the boolean value returned,
  #prints if the user's input is a cube.
  if moduletools.iscube(length, width, height) :
    print("The object is a cube")
  else :
    print("The object is not a cube")


#Calls main function
main()



