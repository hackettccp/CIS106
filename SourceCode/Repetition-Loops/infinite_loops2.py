"""
Demonstrates an Infinite While Loop
"""

#Creates an infinite while loop
while True :

  #Prompts the user to enter a word or phrase.
  #Declares a variable named text and
  #assigns the user's input to it.
  text = input("Enter a word or phrase: ")

  #Breaks out of the loop if the user entered "stop"
  #Any form of exit is accepted (stop, Stop, STOP, etc.)
  if text.lower() == "stop" :
    break

  #Prints the user's entry in uppercase.
  print(text.upper())
