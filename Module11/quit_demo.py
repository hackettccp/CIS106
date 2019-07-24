#Imports the tkinter module
import tkinter
#Imports the tkinter.messagebox module
import tkinter.messagebox

#Main Function
def main() :
	#Creates the window
	test_window = tkinter.Tk()
	#Sets the window's title
	test_window.wm_title("My Window")
	#Creates button that belongs to test_window that
	#calls the showdialog function when clicked.
	test_button = tkinter.Button(test_window,
                                     text="Click Me!",
                                     command=showdialog)

	#Creates button that belongs to test_window that
	#closes/destroys test_window when clicked.
	quit_button = tkinter.Button(test_window,
                                     text="Close Me!",
                                     command= test_window.destroy)

        #Packs the buttons onto the window
	test_button.pack()
	quit_button.pack()
	#Enters the main loop, displaying the window
        #and waiting for events
	tkinter.mainloop()

#Function that displays a dialog box when it is called.
def showdialog() :
	tkinter.messagebox.showinfo("Great Job!", "You pressed the button.")

#Calls the main function/starts the program
main()
