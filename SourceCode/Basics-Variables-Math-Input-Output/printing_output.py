"""
This program demonstrates printing values of variables.

Uncomment each example to see the different ways output can be printed.
"""

#Example 1 - Printing output

#This variable represents a hotel room number
#that a person is staying in. 
room = 503

#These lines print the person's room number
print("I am staying in room number")
print(room)

#Example 2 - Printing on one line of output
"""
#This line prints the person's room number in
#one statement and on one line of output.
print("I am staying in room number", room)
"""

#Example 3 - Printing floats
"""
#This variable represents the maximum speed of
#some vehicle.
top_speed = 160.1

#This variable represents the distance travelled
#by this vehicle
distance = 300.75

#Prints the speed and distance in two lines of output.
print("The top speed is", top_speed)
print("The distance traveled is", distance)
"""

#Example 4 - Removing the default space between items printed.
"""
#This variable represents the balance of a person's account.
dollars = 2.75

#Prints the user's account balance.
print("I have $", dollars, "in my account.")

#Prints the user's account balance but removes spaces between
#each item printed. A space is now needed before the word "in";
#Without it, the dollar amount will run into the word "in".
print("I have $", dollars, " in my account.", sep="")
"""

#Example 5 - Continuation of Example 4
"""
#Assigns a new balance value to the person's account.
dollars = 99.95

#Prints the user's account balance again, removing spaces between
#each item printed.
print("But now I have $", dollars, " in my account!", sep="")
"""
