#Imports the tkinter module
import tkinter

#Main Function
def main() :
        #Creates the window
        test_window = tkinter.Tk()
        #Sets the window's title
        test_window.wm_title("My Window")
        #Creates three labels that belong to test_window
        test_label = tkinter.Label(test_window, text="My Label")
        test_label_2 = tkinter.Label(test_window, text="Hello World!")
        test_label_3 = tkinter.Label(test_window, text="Nice to meet you!")

        #Packs the labels onto the window
        #Since test_label_3 is not packed,
        #it will not be displayed.
        test_label.pack()
        test_label_2.pack()
        
        #Packs the labels onto the window (with orientations)
        #Comment out the previous two pack function calls before
        #uncommenting the three lines below
        #test_label.pack(side="top")
        #test_label_2.pack(side="left")
        #test_label_3.pack(side="left")


        #Enters the main loop, displaying the window
        #and waiting for events
        tkinter.mainloop()

#Calls the main function/starts the program
main()
