"""
Demonstrates using random numbers
"""

#Import the random module
import random

#Get a random number between 1 and 5
#Assign the number to a variable named random_num
random_num = random.randint(1, 5)

#Print the value of random_num
print(random_num)

#********************************#
print()

"""
#Use a for loop to get 10 random numbers between 1 and 10.
#Print the random number selected every iteration
for i in range(10) :
  print(random.randint(1, 10))
"""

#********************************#
print()

"""
#Declare a variable named heads and assign it the value 0
heads = 0

#Declare a variable named tails and assign it the value 0
tails = 0

#Use a for loop to get 10 random numbers between 1 and 2.
#Assign the random number to a variable named r
#If the random number (r) is 1, add 1 to the value of heads
#If the random number (r) is 2, add 1 to the value of tails
for i in range(10) :
  r = random.randint(1, 2)
  if r == 1:
    heads += 1
  else :
    tails += 1

#Print the value of the heads variable
print("Total heads: " + str(heads))

#Print the value of the tails variable
print("Total tails: " + str(tails))
"""
