"""
Demonstrates list slicing.
"""

#Declares a list named numbers containing the values
#50, 40, 20, 30, 70, 10 and 60
numbers = [50, 40, 20, 30, 70, 10, 60]

#Uses list slicing to get the values from indexes 0-3 of the numbers list
#and assigns the slice to a variable named slice1
slice1 = numbers[:4]

#Prints the value of slice1
print(slice1)

#********************************#
print()

"""
#Uses list slicing to get the values starting from index 4 of the numbers list
#and assigns the slice to a variable named slice2
slice2 = numbers[4:]

#Prints the value of slice2
print(slice2)
"""
#********************************#
print()

"""
#Uses list slicing to get the values from indexes 2-5 of the numbers list
#and assigns the slice to a variable named slice3
slice3 = numbers[2:6]

#Prints the value of slice3
print(slice3)
"""
#********************************#
print()

"""
#Uses list slicing to get the values starting from index 1 of the numbers list
#using relative (negative) indexes.
#Assigns the slice to a variable named slice4
slice4 = numbers[-6:]

#Prints the value of slice4
print(slice4)
"""
#********************************#
print()

"""
#Uses list slicing to get the values up to and including index 3 of the numbers list
#using relative (negative) indexes.
#Assigns the slice to a variable named slice5
slice5= numbers[:-3]

#Prints the value of slice5
print(slice5)
"""
#********************************#
print()

"""
#Uses list slicing to get the values from indexes 2-5 of the numbers list
#using relative (negative) indexes.
#Assigns the slice to a variable named slice6
slice6 = numbers[-5:-1]

#Prints the value of slice6
print(slice6)
"""
