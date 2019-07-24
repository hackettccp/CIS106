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
        
	#Creates a global variable for the entry field.
	#It is global in this program so other functions c
	#an access it.
	global test_entry
	#Creates an entry field that belongs to test_window
	test_entry = tkinter.Entry(test_window, width=10)
        
	#Creates button that belongs to test_window that
	#calls the showdialog function when clicked.
	test_button = tkinter.Button(test_window,
                                     text="Click Me!",
                                     command=showdialog)

	#Packs the entry field and button onto the window
	test_entry.pack(side="top")
	test_button.pack(side="top")

	#Enters the main loop, displaying the window
        #and waiting for events
	tkinter.mainloop()

#Function that displays a dialog box when it is called.
#The dialog box will display the text entered in the
#entry field.
def showdialog() :
	tkinter.messagebox.showinfo("Your text", test_entry.get())

#Calls the main function/starts the program
main()

