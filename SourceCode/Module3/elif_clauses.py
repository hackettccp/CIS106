"""
Demonstrates elif clauses
"""

#Prompts the user to enter their test score
#Assigns the user's input to a variable named score.
#Converts the input (a string) to an int.
score = int(input("Enter your test score: "))

#Determines and prints the letter grade for the test score
# A : >90
# B : 80-89
# C : 70-79
# D : 60-69
# F : <59

if(score > 90) :
  print("Your grade is an A.")
elif(score >= 80 and score <= 89) :
  print("Your grade is a B.")
elif(score >= 70 and score <= 79) :
  print("Your grade is a C.")
elif(score >= 60 and score <= 69) :
  print("Your grade is a D.")
else :
  print("Your grade is an F.")

        

