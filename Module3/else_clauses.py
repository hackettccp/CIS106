"""
Demonstrates the else clause
"""

#Prompts the user to enter the water temperature
#Assigns the user's input to a variable named water_temp.
#Converts the input (a string) to an int.
water_temp = int(input("Enter the water temperature: "))

#Prints if the water is frozen or not frozen
#(temperature is less than or equal to 32)
if(water_temp <= 32) :
  print("The water is frozen.")
else :
  print("The water is not frozen.")

        
#********************************#
print()
"""
#Prints if the water is boiling or not boiling
#(temperature is greater than or equal to 212)      
if(water_temp >= 212) :
  print("The water is boiling.")
else :
  print("The water is not boiling.")
"""

#********************************#
print()
"""
#Prints if the water is liquid or not liquid
#(temperature is between to 33 and 211) 
if(water_temp > 32 and water_temp < 212) :
  print("The water is liquid.")
else :
  print("The water is not liquid.")
"""
