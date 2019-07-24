#Imports the tkinter module
import tkinter

#Main Function
def main() :
	#Creates the window
	test_window = tkinter.Tk()
	#Sets the window's title
	test_window.wm_title("My Window")

	#Creates an IntVar for each Checkbutton
	cbvar = tkinter.IntVar()
	cbvar2 = tkinter.IntVar()
	cbvar3 = tkinter.IntVar()

        #Sets each IntVar to zero (unselected)
	cbvar.set(0)
	cbvar2.set(0)
	cbvar3.set(0)

        #Creates three Checkbuttons that belong to test_window and
	#uses their repective IntVar variable.
	testcb = tkinter.Checkbutton(test_window,
                                     text="Option 1",
                                     variable=cbvar)
	testcb2 = tkinter.Checkbutton(test_window,
                                      text="Option 2",
                                      variable=cbvar2)
	testcb3 = tkinter.Checkbutton(test_window,
                                      text="Option 3",
                                      variable=cbvar3)

        #Packs the Checkbuttons onto the window
	testcb.pack()
	testcb2.pack()
	testcb3.pack()

	#Enters the main loop, displaying the window
        #and waiting for events
	tkinter.mainloop()

#Calls the main function/starts the program
main()
