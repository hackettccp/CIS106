"""
Demonstrates using a module
"""
#Import the spheretools module
import spheretools

def main() :
  #Prompt the user to enter a radius
  #Store the input (as an int) to a variable named radius
  radius = int(input("Enter a radius: "))

  #Pass the radius variable as an argument to the
  #spheretools' get_surface_area function. Assign the value returned to
  #a variable named surface_area
  surface_area = spheretools.getsurfacearea(radius)

  #Pass the radius variable as an argument to the
  #spheretools' getVolume function. Assign the value returned to
  #a variable named volume
  volume = spheretools.getvolume(radius)

  #Print the values of the surfacearea and volume variables
  print("The surface area is", surface_area)
  print("The volume is", volume)


#Calls main function
main()



