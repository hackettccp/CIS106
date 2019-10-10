# RUN THE write_emp_records.py PROGRAM FIRST!
# That program will create the employees.txt file
# this program uses.

# After running this program, check the employees.txt file in Notepad
# (Or a similar text editor) to see that the values were appended to the file.

def main():
    
    # Open a file for writing.
    emp_file = open("employees.txt", "a")

    # Get the number of employee records to create.
    choice = input("Do you want to add additional employees? " + \
                         "(y for yes): "))

    # Get each employee"s data and write it to
    # the file.
    while choice == "y":
        # Get the data for an employee.
        print("Enter data for employee #", count, sep="")
        name = input("Name: ")
        id_num = input("ID number: ")
        dept = input("Department: ")

        # Write the data as a record to the file.
        emp_file.write(name + "\n")
        emp_file.write(id_num + "\n")
        emp_file.write(dept + "\n")

        # Display a blank line.
        print()

    # Close the file.
    emp_file.close()
    print("Employee records written to employees.txt.")

# Call the main function.
main()




