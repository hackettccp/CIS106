#Imports the tkinter module
import tkinter

#Main Function
def main() :
	#Creates the window
	test_window = tkinter.Tk()

	#Sets the window's title
	test_window.wm_title("My Window")

	#Enters the main loop, displaying the window
	#and waiting for events
	tkinter.mainloop()

#Calls the main function/starts the program
main()
