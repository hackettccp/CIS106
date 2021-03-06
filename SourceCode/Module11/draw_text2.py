"""
Demonstrates drawing text on a canvas.
"""
#Imports the tkinter module
import tkinter

def main() :
    #Creates the window
    test_window = tkinter.Tk()
    #Sets the window's title
    test_window.wm_title("Text Example 2")

    #Creates the Canvas widget.
    canvas = tkinter.Canvas(test_window,
                            width=160,
                            height=160,
                            background="cyan")

    #Draws a polygon (octogon).
    canvas.create_polygon(60, 20,
                          100, 20,
                          140, 60,
                          140, 100,
                          100, 140,
                          60, 140,
                          20, 100,
                          20, 60,
                          fill="red")

    #Display text in the center of the canvas.
    #Drawn on top of the polygon
    canvas.create_text(80, 80,
                       text="STOP",
                       font=("Arial", 32),
                       fill="white")
    
    #Packs the canvas onto the window
    canvas.pack()
        
    #Enters the main loop, displaying the window
    #and waiting for events
    tkinter.mainloop()

#Calls the main function
main()
