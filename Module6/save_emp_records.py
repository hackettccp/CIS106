# RUN THIS PROGRAM BEFORE RUNNING read_emp_records.py or append_emp_records.py!
# Both programs require the employees.txt file
# this program creates.

# After running this program, check the employees.txt file in Notepad
# (Or a similar text editor) to see that the values were written to the file.

# This program gets employee data from the user and
# saves it as records in the employee.txt file.

def main():
    # Get the number of employee records to create.
    num_emps = int(input("How many employee records " + \
                         "do you want to create? "))

    # Open a file for writing.
    emp_file = open("employees.txt", "w")

    # Get each employee"s data and write it to
    # the file.
    for count in range(1, num_emps + 1):
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

    
