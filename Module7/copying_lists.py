"""
Demonstrates copying lists
"""

#Declares a list named numbers containing the values 1, 2, 3 and 4
numbers = [1, 2, 3, 4]

#Creates a shallow copy of the numbers list named numbers2
numbers2 = numbers

#Changes the first element of the numbers2 list to 100
numbers2[0] = 100

#Prints the numbers list
print(numbers)

#********************************#
print()

"""
#Declares a list named scores containing the values 80.5, 75.4, 90.15 and 86.75.
scores = [80.5, 75.4, 90.15, 86.75]
        
#Declares an empty list named scores2
scores2 = []
        
#Copies each element from the scores list to the scores2 list
#using a for loop.
for s in scores:
  scores2.append(s)

#Changes the third element of the scores list to 93.25
scores[2] = 93.25;
        
#Prints both lists
print(scores)
print(scores2)
"""
#********************************#
print()

"""
#Declares a list named values containing the values 5, 7, 3 and 1
values = [5, 7, 3, 1]
        
#Declares a list named values2 and assigns it a deep copy of the values list
values2 = [] + values
        
#Prints the values2 list
print(values2)
"""
