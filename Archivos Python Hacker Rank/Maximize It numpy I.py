
#-------------------------------------------------------------------------------

import numpy as np
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
# Make the list inside if ll equal in length using compression list
n = len(max(ll,key=len)) # Calculate length of maximal list
ll2 = [x+[0]*(n-len(x)) for x in ll]
# Convert list ll2 to numpy array using np.array(ll2) and apply the function x^2
# using arithmetic property to every element in the array get the square value
# using bb**2 or the function pow(bb,2)
bb = np.array(ll2)
aa = pow(bb,2)
# The print func,in lines 46-48 is no required is used for improve output
print(36*"*")
print(12*' ' + 'ouput:' + 12*' ')
print('')
print(max([sum(map(lambda x:x,i))%m for i in product(*aa)]))