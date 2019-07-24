"""
Demonstrates converting strings to ints and floats.
"""

#Example 1 - Converting a string-type to an int.

#Declares a variable named str_value1 and assigns it the string literal "101"
str_value1 = "101"

#Declares a variable named int_value1 and assigns it the value 52
int_value1 = 52

#Declares a variable named total1
#Assigns to it the sum of str_value1 (as an int) and int_value1
#str_value1 is still a string-type. The int function returns the int value
#taken from the string.
total1 = int(str_value1) + int_value1

#Prints the value of total1
print(total1)

#********************************#
print()

#Example 2 - Converting a string-type to a float.

"""
#Declares a variable named str_value2 and assigns it the string literal "102.7"
str_value2 = "102.7"

#Declares a variable named int_value2 and assigns it the value 43
int_value2 = 43

#Declares a variable named total2
#Assigns to it the difference of str_value2 (as a float) and int_value2
#str_value2 is still a string-type. The float function returns the float value
#taken from the string.
total2 = float(str_value2) - int_value2

#Prints the value of total2
print(total2)
"""

#********************************#
print()

#Example 3 - ValueError exceptions
#A ValueError will occur if you try to convert a non-numeric string
#to an int or float.
"""
#Declares a variable named str_value3 and assigns it the string literal "102.7 FM"
str_value3 = "102.7 FM"

#Declares a variable named float_value1 and attempts to assign to it
#str_value3 returned as a float. This will not work and will cause an exception,
#stopping the program.
float_value1 = float(str_value3)

#The same thing would happen if we tried to convert str_value3 to an int.
#Additionally, "102.7" could not be converted to an int because it contains
#a period. This is ok when converting to a float because the period represents
#the decimal place.
"""
