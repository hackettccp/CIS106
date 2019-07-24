"""
Demonstrates what happens when you change the value of a parameter.
"""

def main():
    value = 99
    print("The value is", value)
    changeme(value)
    print("Back in main the value is", value)

def changeme(arg):
    print("I am changing the value.")
    arg = 0 #Does not affect the value variable back in the main function.
    print("Now the value is", arg)

#Calls the main function.
main()
