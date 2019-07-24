#Imports the tkinter module
import tkinter

#Main Function
def main() :
        #Creates the window
	test_window = tkinter.Tk()
	#Sets the window's title
	test_window.wm_title("My Window")
	#Creates five labels that belong to test_window
	test_label = tkinter.Label(test_window, text="Top")
	test_label_2 = tkinter.Label(test_window, text="Bottom")
	test_label_3 = tkinter.Label(test_window, text="Left")
	test_label_4 = tkinter.Label(test_window, text="Right")
	test_label_5 = tkinter.Label(test_window, text="Center")
        
        #Packs the labels onto the window (with orientations)
	test_label.pack(side="top")
	test_label_2.pack(side="bottom")
	test_label_3.pack(side="left")
	test_label_4.pack(side="right")
	test_label_5.pack() #No side argument defaults to center
        
	#Enters the main loop, displaying the window
        #and waiting for events
	tkinter.mainloop()
        
#Calls the main function/starts the program
main()
