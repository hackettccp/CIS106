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

        #Creates a global IntVar variable.
	#This will be shared among the members
	#of a radio button group.
	#It is global in this program so other functions
	#can access it.
	global rbvar
	rbvar = tkinter.IntVar()
        #Sets the IntVar to zero (none selected)
	rbvar.set(0)

        #Creates three Radiobuttons that belong to upper_frame and
	#uses the shared IntVar variable.
	#Each Radiobutton has a unique value. This value will tell us which
	#button is currently selected.
	testrb = tkinter.Radiobutton(upper_frame,
                                     text="Option 1",
                                     variable=rbvar,
                                     value=1)
	testrb2 = tkinter.Radiobutton(upper_frame,
                                      text="Option 2",
                                      variable=rbvar,
                                      value=2)
	testrb3 = tkinter.Radiobutton(upper_frame,
                                      text="Option 3",
                                      variable=rbvar,
                                      value=3)

        #Packs the Radiobuttons onto upper_frame
	testrb.pack()
	testrb2.pack()
	testrb3.pack()

        #Creates a button that belongs to lower_frame and calls the
	#showdialog function when clicked.
	ok_button = tkinter.Button(lower_frame,
                                  text="Get Selection",
                                  command=showdialog)

	#Creates a button that belongs to lower_frame and calls the
	#reset function when clicked.
	reset_button = tkinter.Button(lower_frame,
                                     text="Reset",
                                     command=reset)

	#Creates a button that belongs to lower_frame and calls test_window's
	#destroy function when clicked.
	quit_button = tkinter.Button(lower_frame,
                                    text="Quit",
                                    command=test_window.destroy)

        #Packs the three buttons onto lower_frame
	ok_button.pack(side="left")
	reset_button.pack(side="left")
	quit_button.pack(side="left")

        #Packs the frames onto the window
	upper_frame.pack()
	lower_frame.pack()

	#Enters the main loop, displaying the window
        #and waiting for events
	tkinter.mainloop()

#Function that displays a dialog box when it is called.
#The function builds a string based on which Radiobutton is selected.
#The dialog box will display the string created.
def showdialog() :
        output = "You selected:\n"
        #The IntVar variable's get function will return the value of the
        #Radiobutton that is currently selected
        if rbvar.get() == 0 :
                output += "None"
        elif rbvar.get() == 1 :
                output+= "Option 1"
        elif rbvar.get() == 2 :
                output+= "Option 2"
        elif rbvar.get() == 3 :
                output+= "Option 3"
        tkinter.messagebox.showinfo("Selections", output)

#Function that sets the rbvar IntVar variable back to zero.
#0 doesn't correspond to any of the Radiobuttons' values,
#so none will be selected.
def reset() :
        rbvar.set(0)

#Calls the main function/starts the program
main()
