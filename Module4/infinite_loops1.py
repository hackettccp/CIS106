#This program demonstrates an infinite loop.
#Create a variable to control the loop.
keep_going = "y"

#Warning! Infinite loop! This program will never end.
while keep_going == "y":
    #Get a salesperson"s sales and commission rate.
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))

    #Calculate the commission.
    commission = sales * comm_rate

    #Display the commission.
    print("The commission is $", \
          format(commission, ",.2f"), sep="")

#Since keep_going never changes in the body of the loop,
#the loop's condition will always be true.
