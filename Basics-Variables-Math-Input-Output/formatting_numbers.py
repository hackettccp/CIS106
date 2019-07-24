"""
Demonstrates how numbers can be displayed with formatting.

The format function always returns a string-type, regardless
of if the value to be formatted is a float or int.
"""

#Example 1 - Formatting floats
amount_due = 15000.0
monthly_payment = amount_due / 12
print("The monthly payment is $", monthly_payment)
#Formatted to two decimal places
print("The monthly payment is $", format(monthly_payment, ".2f"))
#Formatted to two decimal places and includes commas
print("The monthly payment is $", format(monthly_payment, ",.2f"))
print("The monthly payment is $", format(monthly_payment, ',.2f'), sep="")

#********************************#
print()

#Example 2 - Formatting ints

"""
weekly_pay = 1300
annual_salary = weekly_pay * 52
print("The annual salary is $", annual_salary)
print("The annual salary is $", format(annual_salary, ",d"))
print("The annual salary is $", format(annual_salary, ",d"), sep="")
"""

#********************************#
print()

#Example 3 - Scientific Notation

"""
distance = 567.465234
print("The distance is", distance)
print("The distance is", format(distance, ".5e"))
"""

#********************************#
print()

#Example 4 - Formatting floats

# This example displays the following
# floating-point numbers in a column
# with their decimal points aligned.
"""
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Display each number in a field of 7 spaces
# with 2 decimal places.
print(format(num1, '7.2f'))
print(format(num2, '7.2f'))
print(format(num3, '7.2f'))
print(format(num4, '7.2f'))
print(format(num5, '7.2f'))
print(format(num6, '7.2f'))
"""
