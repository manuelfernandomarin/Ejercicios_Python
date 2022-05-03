#-------------------------------------------------------------------------------
# Name: Finding the percentage        module1
# Purpose: The code will read in a dictionary containing key/value pairs of
# name:[marks] for a list of students. Print the average of marks array for name
# provided, showing 2 places after the decimal.
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


if __name__ == '__main__':
    n = int(input()) # define the number of students
    student_marks = {} # declare a dictionary
    # Using a recursion loop for evry student to request user's data input
    for _ in range(n) :
        # assign student's name to var name and each numrical values to var line
        name, *line = input().split()
        # create a list called score with numerical floating values
        scores = list(map(float, line))
        # assign  to dictionary to every name (key) the records (value)
        student_marks[name] = scores
    # request user' data to define the student to get the average of records
    query_name = input()
    # Process to calculate and print the average
    if query_name in student_marks:
        query_records = student_marks[query_name]
        avg = sum(query_records)/len(query_records)
        # The first next print function are used to improve the answer
        # no required in the problem
        print(len("The average of records to " + query_name + " is") * '*')
        print("The average of records to " + query_name + " is")
        print(format(avg, '.2f'))




