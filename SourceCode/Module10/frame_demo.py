#Imports the tkinter module
import tkinter

#Main Function
def main() :
        #Creates the window
	test_window = tkinter.Tk()
	#Sets the window's title
	test_window.wm_title("My Window")
	#Creates two frames (both belong to test_window)
	upper_frame = tkinter.Frame(test_window)
	lower_frame = tkinter.Frame(test_window)

        #Creates two labels (both belong to upper_frame)
	label1 = tkinter.Label(upper_frame, text="Label 1")
	label2 = tkinter.Label(upper_frame, text="Label 2")
        
	#Creates two labels (both belong to lower_frame
	labelA = tkinter.Label(lower_frame, text="Label A")
	labelB = tkinter.Label(lower_frame, text="Label B")

        #Packs each label on their frame with an orientation
	label1.pack(side="top")
	label2.pack(side="top")
	labelA.pack(side="left")
	labelB.pack(side="left")

        #Packs each of the frames to the window
	upper_frame.pack()
	lower_frame.pack()

        #Enters the main loop, displaying the window
        #and waiting for events
	tkinter.mainloop()

#Calls the main function/starts the program	
main()
