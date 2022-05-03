#-------------------------------------------------------------------------------
# Name: Zipped       module1
# Purpose: The function zip([iterable, ...]) returns a list of tuples. The ith
# tuple contains ith elemet from each of the argument  sequences or iterables.
# If the argument sequencews are of unequal lengths, then the returned list is
# truncated of rhe shortest argument sequence.
# Task: The National University conducts an examination of N students in
# X subjects. Yout task is compute the average scores of each student
# (Sum of scores obtained in all subject by student) = DD
# (Totalnumber of subjets) = SS
#  Average score = DD/SS
# The format of general marks is: Columns --> Student ID; Row --> Subject Name
# Input format The first input line contains N and X separated by space
# The next X lines contains the space sepated marks obtained by students in
# particular subject
# Ouput fromat Print averages of all students on separated lines. The averages
# must to be correct up to 1 decimal place
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input().split()[1]) # assing the requested number of subjects
for s in zip(*(input().split() for _ in range(x))):
    print("%0.1f"%(sum(map(float,s))/x))

# Notes:
# n represents the number of stundents, x is the marks obteined in each subjects
# the user's data input have two components l=[n,x], where l[0] = n colunms,
# l[1] = x rows then in bucle for, for every colums that is very studens,
# sum very marks in every subject and divide sum/number of subject
