#This program calculates the sum of a series
#of numbers entered by the user.

limit = 5   #The maximum number

#Initialize an accumulator variable.
total = 0.0
   
#Explain what we are doing.
print("This program calculates the sum of")
print(limit, "numbers you will enter.")

#Repeats 5 times (based on the value of the limit variable)
for counter in range(limit):
    #Asks the user to enter a number to be added to the total
    number = int(input("Enter a number: "))
    #Adds the number entered to a running total/accumulator
    total = total + number

#Display the total of the numbers.
print("The total is", total)


