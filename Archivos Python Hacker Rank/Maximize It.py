#-------------------------------------------------------------------------------
# Name: Maximize It        module1
# Purpose: You are given a finction f(x) = X^2. You are also given K lists.
# The i^th list consists of N, elements. You have to pick one element from each
# list so that the value from the equation below is maximized:
# S = (f(X1) + f(X2)+...+f(Xk))%M; where Xi denotes the element picked from the
# i^th list. Find the maximized value Smax obtained.
# Note that need take exactly one element from each list, not necessarly the
# largest element. You add the squares of the chosen elements and perform the
# modulo operation. The maximum value that you can obtain, will be the answer to
# the problem.
# Input format: The first line contains 2 space separated integer K and M.
# The next K lines each contains an integer N, denoting the number of elements
# in the i^th list, followed by N, space separated integers denoting the
# elements in the list. Contrains: 1<=K<=7; 1<=M<=1000; 1<=Ni<=7;
# 1<=Magnitude of elementsin list <= 10^9
# Output Format: Output a single integer denoting the value Smax
#
# Author:      tioFer
#
# Created:     23/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
# In this case the number of list (k) and denominator value (m) using funtion
# map due the user's data input are two integers values whit a space between
# value and value
k,m = map(int,input().split())
# To every user's data input (k) is used a loop for in a list called ll, using
# funtion slpit() to separate every data input for list, every data have a blank
# space like # separator
ll = [list(map(int,input().split())) for _ in range(k)]
# Due user's data input to every list, the first data is the number line, the
#  other data are the elements of very list
aa = map(lambda p : p[1:],ll)
# The print func,in lines 40-42 is no required is used for improve output
print(36*"*")
print(12*' ' + 'ouput:' + 12*' ')
print('')
print(max([sum(map(lambda x:x**2,i))%m for i in product(*aa)]))
