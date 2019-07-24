"""
Demonstrates nested loops.

This program displays a rectangular pattern or asterisks.
"""
#Prompt the user for the number of rows and columns
rows = int(input("How many rows? "))
cols = int(input("How many columns? "))

#This variable will be used to build each row of asterisks
line = ""

#Loop for every row
for r in range(rows):
    #Loop for each column in the row
    for c in range(cols):
        #Append one asterisk for the row
        line += "*"
    #Print the row of asterisks
    print(line)
    #Reset for the next row
    line = ""
