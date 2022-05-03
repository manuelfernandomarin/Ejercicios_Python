#-------------------------------------------------------------------------------
# Name: Nested Lists       module1
# Purpose: Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s)
# having the second lowest grade
# Note: If there are multiple students with the second lowest grade, order
# their names alphabetically and print each name on a new line.
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


if __name__ == '__main__':
    n = int(input()) # request the numbers of Students in a class or subject
    ms = []  # define list named: ms
    # Process to store name and grades for every student these datas are given
    # in a list, to be store like ekement of list ms
    # Note: the user's data input, the name of student is provided followed by
    # the record or score of these subject
    ms = [[input(), float(input())] for _ in range(n)]
    # Get the second lowest score or record
    sh = sorted(list(set([xx for buny, xx in ms])))
    p = sh[1] # Assign to var p the second lowest score
    # Generate the list of names with second lowest score
    s = [x for x, y in ms if y==p]
    # improve the output this is no required in the orignal problem
    print(len("The name of student(s) with de second lower score")*"*")
    print("The name of student(s) with de second lower score")
    # Generate the answer printing the name of students per line
    for name in sorted(s) :
        print(name, end='\n')






