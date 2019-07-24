#Imports the tkinter.messagebox module
import tkinter.messagebox

#Main Function
def main() :
        #Displays a pop-up dialog box.
	tkinter.messagebox.showinfo("My Dialog", "I am a Dialog")

	#The text below will not print
	#until the dialog box created above is closed.
	print("Dialog is closed.")

#Calls the main function/starts the program	
main()
