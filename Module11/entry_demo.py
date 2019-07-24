#Imports the tkinter module
import tkinter

#Main Function
def main() :
	#Creates the window
	test_window = tkinter.Tk()
	#Sets the window's title
	test_window.wm_title("My Window")

	#Creates an entry field that belongs to test_window
	test_entry = tkinter.Entry(test_window, width=10)

        #Packs the entry field onto the window
	test_entry.pack()
	#Enters the main loop, displaying the window
        #and waiting for events
	tkinter.mainloop()

#Calls the main function/starts the program
main()
