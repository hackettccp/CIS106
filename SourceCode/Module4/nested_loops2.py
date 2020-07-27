# This program averages test scores. It asks the user for the
# number of students and the number of test scores per student.

# Get the number of students.
num_students = int(input("How many students do you have? "))

# Get the number of test scores per student.
num_test_scores = int(input("How many test scores per student? "))

#Determine each students average test score.
#This loop repeats for every student
for student in range(num_students):
    #Initialize an accumulator variable for the student's test scores.
    total = 0.0
    #Get the student's test scores.
    #(Need to add one because the loop will start at zero)
    print("Student number", student + 1)
    print("-----------------")
    #Repeats for every test score
    for test_num in range(num_test_scores):
        #Prompts the user to enter the test score
        score = float(input("Test number" + str(test_num + 1) + ": "))
        # Add the score to the accumulator.
        total += score

    #Calculate the average test score for this student.
    average = total / num_test_scores

    #Display the average.
    print("The average for student number", student + 1, "is:", format(average, ".1f"))
    print()



        
