"""
Demonstrates writing to a file sequentially
"""

#Opens a new file (Python will automatically create it)
#named outputfile.txt in write mode.
#Assigns the file to a variable names file_to_write
file_to_write = open("outputfile.txt", "w")

#Uses a loop to prompt the user to enter any input.
while True:
  line = input("Enter some text: ")
  if line.lower() == "exit" :
    #If the user enters the word "exit", the loop stops
    break
  else :
    #Writes the user's input to the open file
    #Adds a linefeed when writing each line of input to the file
    file_to_write.write(line + "\n")

#Closes/saves the file
file_to_write.close()

#If you run this program again, the existing text of outputfile.txt
#will be deleted and replaced with the new data this program will
#provide.






