#-------------------------------------------------------------------------------
# Name: Any or All      module1
# Purpose: Function any(), this expression returns True if any elements of the
# iterable is true. If the iterable is empty, it will return False.
# The function all() returns True if all of the elemts of the iterable are true.
# If will return True.
# Task You are given a space separated list of integers. If all the integers are
# positive, then you need to check if any integer is a palindrome integer.
# Input Format: The first line contains an integer N. N is the total number of
# integers in the list. The second line contains the space separated list of N
# integers. Constraints 0<N<100. Output Format: Print True if all conditions of
# the problem statement are satisfied. Otherwise, print False.
#
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
# asign user's data input, to N, a integer value, to n a list of integer values
# separate space
N,n=int(input()),input().split()
# nn1 is true if all elements is True
nn1=all([int(i)>0 for i in n])
# nn2 is tue if any elements is True
nn2=any([j==j[::-1] for j in n])
print(nn1 and nn2)
