#Imports the tkinter module
import tkinter

#Main Function
def main() :
	#Creates the window
	test_window = tkinter.Tk()
	#Sets the window's title
	test_window.wm_title("My Window")

	#Creates a global StringVar variable.
	#It is global in this program so other functions
	#can access it.
	global label_text
	label_text = tkinter.StringVar()

	#Sets the StringVar's text value
	label_text.set("Original Text")

	#Creates label that belongs to test_window and
	#uses the label_text StringVar
	test_label = tkinter.Label(test_window,
                                   textvariable=label_text)

	#Creates button that belongs to test_window that
	#calls the changetext function when clicked.
	test_button = tkinter.Button(test_window,
                                     text="Change Text",
                                     command=changetext)

	#Packs the label and button onto the window
	test_label.pack()
	test_button.pack()
	#Enters the main loop, displaying the window
        #and waiting for events
	tkinter.mainloop()

#Function that sets a nex text value to the label_text StringVar
def changetext() :
	label_text.set("New Text")

#Calls the main function/starts the program	
main()





