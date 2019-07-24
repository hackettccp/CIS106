"""
Demonstrates reading a file sequentially
"""

#Opens the readfile.txt file in read-only mode
#Assigning the file to a variable named file_to_read
file_to_read = open("friends.txt", "r")

#Assigns the entire contents (one long string) of the file
#to a variable named contents
contents = file_to_read.read()

#Prints the value of the contents variable
print(contents)

#Closes the file_to_read variable
file_to_read.close()

#********************************#
print()

"""
#Opens the readfile.txt file in read-only mode
#Assigning the file to a variable named file_to_read2
file_to_read2 = open("friends.txt", "r")

#Uses the file_to_read2 variable's readline function to assign the
#first line of the file to a variable named line
line = file_to_read2.readline()

#Prints the value of the line variable
print(line)

#Uses the file_to_read2 variable's readline function again to assign the
#next line of the file to the line variable
line = file_to_read2.readline()

#Prints the value of the line variable
print(line)

#Closes the file_to_read2 variable
file_to_read2.close()
"""

#********************************#
print()

"""
#Opens the readfile.txt file in read-only mode
#Assigns the file to a variable named file_to_read3
file_to_read3 = open("friends.txt", "r")

#Uses a loop to iterate over the lines of text of the file and
#print each line. 
for line in file_to_read3 :
  #Strips away any linefeed escape sequences before printing
  print(line.rstrip("\n"))

#Closes the file_to_read3 variable
file_to_read3.close()
"""

#********************************#
print()

"""
#Opens the numbers.txt file (in the testFolder directory) in read-only mode
#Assigns the file to a variable named file_to_read4
file_to_read4 = open("testFolder//numbers.txt", "r")

#Declares a variable named total and assign it the value 0
total = 0

#Uses a loop to iterate over the lines of text in the file (each line contains
#a number).
for line in file_to_read4 :
  #Uses the total variable to keep a running total (sum)
  #of the numbers contained in the file.
  #Strips away any linefeed escape sequences
  total += int(line.rstrip("\n"))

#Prints the value of the total variable
print(total)

#Closes the file_to_read4 variable
file_to_read4.close()
"""
