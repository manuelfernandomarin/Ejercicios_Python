#-------------------------------------------------------------------------------
# Name: Input      module1
# Purpose: You are given a polynomial P of a single indeterminate
# (or variable), x. You are also given the values of x and k. Your
# task is to verufy if P(x)=k
# All coefficients of polynomial P are integers, also x and y are also integers.
# Input format: the first line contains the space separated values of x and k.
# The second line contains the polynomial P.
# Output Print True if P(x)=k. Otherwise, print False.
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
# assign the first two user's data input for valus x and k
x,k=list(map(int,input().split(" ")))
# assign the polinomial to variable P
P=input()
# Print evaluate the answer given by polinomial and value k
print(eval(P)==k)
