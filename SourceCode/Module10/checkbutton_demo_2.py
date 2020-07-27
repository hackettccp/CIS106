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

	#Creates two frames that belong to test_window
	upper_frame = tkinter.Frame(test_window)
	lower_frame = tkinter.Frame(test_window)

        #Creates three global IntVar variables.
	#One for each checkbutton.
	#They are global in this program so other functions
	#can access them.
	global cbvar
	global cbvar2
	global cbvar3
	cbvar = tkinter.IntVar()
	cbvar2 = tkinter.IntVar()
	cbvar3 = tkinter.IntVar()

	#Sets each IntVar to zero (unselected)
	cbvar.set(0)
	cbvar2.set(0)
	cbvar3.set(0)

        #Creates three Checkbuttons that belong to upper_frame and
	#uses their repective IntVar variable.
	testcb = tkinter.Checkbutton(upper_frame,
                                     text="Option 1",
                                     variable=cbvar)
	testcb2 = tkinter.Checkbutton(upper_frame,
                                      text="Option 2",
                                      variable=cbvar2)
	testcb3 = tkinter.Checkbutton(upper_frame,
                                      text="Option 3",
                                      variable=cbvar3)

        #Packs the Checkbuttons onto upper_frame
	testcb.pack()
	testcb2.pack()
	testcb3.pack()

        #Creates a button that belongs to lower_frame and calls the
	#showdialog function when clicked.
	ok_button = tkinter.Button(lower_frame,
                                  text="Get Selections",
                                  command=showdialog)
        #Creates a button that belongs to lower_frame and calls test_window's
	#destroy function when clicked.
	quit_button = tkinter.Button(lower_frame,
                                    text="Quit",
                                    command=test_window.destroy)

        #Packs the two buttons onto lower_frame
	ok_button.pack(side="left")
	quit_button.pack(side="left")

        #Packs the frames onto the window
	upper_frame.pack()
	lower_frame.pack()

	#Enters the main loop, displaying the window
        #and waiting for events
	tkinter.mainloop()

#Function that displays a dialog box when it is called.
#The function builds a string based on which Checkbuttons are selected.
#The dialog box will display the string created.
def showdialog() :
        output = "You selected:\n"
        #If the IntVar variable's get function returns 1, that means
        #the Checkbutton is currently selected/checked
        if cbvar.get() == 1 :
                output+= "Option 1\n"
        if cbvar2.get() == 1 :
                output+= "Option 2\n"
        if cbvar3.get() == 1 :
                output+= "Option 3\n"
        if cbvar.get() == cbvar2.get() == cbvar3.get() == 0 :
                output += "None"
        tkinter.messagebox.showinfo("Selections", output)

#Calls the main function/starts the program
main()
