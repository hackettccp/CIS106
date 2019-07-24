"""
Demonstrates keyboard input.
"""

#Prompts the user to enter their name
#Assigns their input to a variable named name
name = input("Enter your name: ")
        
#Prompts the user to enter their street address
#Assigns their input to a String variable named address
address = input("Enter your street address: ")

        
#Prompts the user to enter their city
#Assigns their input to a variable named city
city = input("Enter your city: ")
        
#Prompts the user to enter their state
#Assigns their input to a variable named state
state = input("Enter your state: ")
        
#Prompts the user to enter their zip code
#Assigns their input to a variable named zip_code
zip_code = input("Enter your zip code: ")

#Prints a blank line
print()

#Prints out the user's information:
#First Line:  Their name
#Second Line: Their street address
#Third Line:  City, State, Zip Code
print(name)
print(address)
print(city + ", " + state + " " + zip_code)
