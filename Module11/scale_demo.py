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


        #Creates two global variables for the scales.
	#They are global in this program so other functions
	#can access them.
	global vscale
	global hscale

	#Creates a scale that belongs to upper_frame, starts at
	#0 and ends at 50
	vscale = tkinter.Scale(upper_frame,
                               from_=0,
                               to=50)
        #Creates a scale that belongs to upper_frame, starts at
	#0, ends at 200, displays tick marks at every tenth interval,
	#and is oriented horizontal
	hscale = tkinter.Scale(upper_frame,
                               from_=0,
                               to=200,
                               tickinterval=10,
                               length=500,
                               orient="horizontal")

        #Sets the hscale scale at 90
	hscale.set(90)


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

        #Packs the scales onto upper_frame 
	vscale.pack()
	hscale.pack()
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
#The function builds a string based on values currenlty selected
#on both scales.
#The dialog box will display the string created.
def showdialog() :
        output = "You selected:\n"
        output += "vscale: " + str(vscale.get()) + "\n"
        output += "hscale: " + str(hscale.get())
        tkinter.messagebox.showinfo("Selections", output)

#Function that sets the scales to zero.
def reset() :
        vscale.set(0)
        hscale.set(0)

#Calls the main function/starts the program
main()
