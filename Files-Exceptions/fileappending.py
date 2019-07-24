"""
Demonstrates appending to a file
"""

#Opens the existing file (in append mode) named outputfile.txt
#in append mode.
#Assigns this file to a named variable file_to_append
file_to_append = open("outputfile.txt", "a")

#Uses a loop that prompts the user to enter input.
#Since the file is opened in append mode, the data will be added
#to the file; Existing data in the file will not be deleted.
while True:
  line = input("Enter some text: ")
  
  if line.lower() == "exit" :
    #If the user enters the word "exit", the loop stops
    break
  else :
    #Write sthe user's input to the file
    #Adds a linefeed when writing each line of input to the file
    file_to_append.write(line + "\n")

#Close/save the file_to_append variable
file_to_append.close()
