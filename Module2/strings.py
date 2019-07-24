"""
Demonstrates the string type

Uncomment each section to demonstrate different string operations.
"""

#Example 1 - Declaration, Assignment, and Reassignment.

#Declares a variable named my_greeting
#Assigns it the string literal "Hello World"
my_greeting = "Hello World!"

#Prints the value of my_greeting
print(my_greeting)

"""
#Assigns the string literal "Hi There!" to the my_greeting variable
my_greeting = "Hi there!"

#Prints the value of my_greeting
print(my_greeting)
"""
#********************************#
print()

#Example 2 - Concatenation

"""
#Declares 3 variables named united, states, and of_america
#Assigns the string literals "United ", "States ", and "of America" to their
#respective variables
united = "United "
states = "States "
of_america = "of America"

#Declares a variable named usa1
#Concatenates the united, states, and of_america together and
#assign the result to the usa1 variable.
usa1 = united + states + of_america
        
#Prints the value of the usa1 variable
print(usa1)

#Prints a blank line
print()

#Prints the values of the original 3 variables to show
#their individual values have not changed
print(united)
print(states)
print(of_america)
"""
#********************************#
print()

#Example 3 - Appending

"""
#Declares a variable named usa2
#Assigns usa2 an empty string
usa2 = ""
        
#Appends the value of united to usa2.
usa2 += united
        
#Appends the value of states to usa2.
usa2 += states

#Appends the value of of_america to usa2.
usa2 += of_america
        
#Prints the value of the usa2 variable.
print(usa2)

#Prints a blank line
print()

#Prints the values of the original 3 variables to show
#their individual values have not changed
print(united)
print(states)
print(of_america)
"""
#********************************#
print()

#Example 4 - Converting to uppercase

"""
#Declares a variable named usa_uppercase
#Assigns to it the usa1 variable in uppercase
usa_uppercase = usa1.upper()

#Prints the value of the usa1 variable.
#The upper function does not change the string/variable it
#is called on; It simply returns an uppercase version of itself.
print(usa1)

#Prints the value of the usa_uppercase variable.
print(usa_uppercase)
"""
#********************************#
print()

#Example 5 - Converting to lowercase

"""
#Declares a variable named usa_lowercase
#Assigns to it the usa_uppercase variable in lowercase
usa_lowercase = usa_uppercase.lower()

#Prints the value of the usa_uppercase variable.
#The lower function does not change the string/variable it
#is called on; It simply returns a lowercase version of itself.
print(usa_uppercase)

#Prints the value of the usa_lowercase variable.
print(usa_lowercase)
"""
