"""
Demonstrates validating a user's entry/input
"""

mark_up = 2.5  #The markup percentage
another = "y"  #Variable to control the loop.

#Process one or more items.
while another == "y" or another == "Y":
    #Get the item's wholesale cost from the user.
    wholesale = float(input("Enter the item's wholesale cost: "))

    #Validate the wholesale cost entered by the user.
    #Ask the user to re-enter their input as long as their
    #entry is negative.
    while wholesale < 0:
        print("ERROR: the cost cannot be negative.")
        wholesale = float(input("Enter the correct wholesale cost:"))

    #Calculate the retail price.
    retail = wholesale * mark_up

    #Display the retail price.
    print("Retail price: $", format(retail, ",.2f"), sep="")


    #Do this again?
    #If the user enters y or Y the loop will repeat.
    another = input("Do you have another item? (Enter y for yes): ")
