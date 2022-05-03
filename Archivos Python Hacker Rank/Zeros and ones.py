#-------------------------------------------------------------------------------
# Name:  Zeros and ones      module1
# Purpose: You are given the shape of the array in the form of space-separated
# integers, each integer representing the size of different dimensions, your
# task is to print an array of the given shape and integer type using the tools
# numpy.zeros and numpy.ones.
# Input Format: A single line containing the space separated integers.
# Constrains; 1<= each integer <= 3
# Output Format: First, print array using the numpy.zeros tool and then print
# the array with the numpy.ones tool.
#
# Author:      tioFer
#
# Created:     26/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
21
import numpy as np

# Proces to capture nad store the data input in a list
# Using a compresion list in intead of list(map(int, input().split()))
L = [int(x) for x in input().split()]
# Loop to verify that user's data input 1<=data input<=3
for t in range(len(L)):
    if L[t] < 1 or L[t] > 3 :
       print ('Data input', L[t], 'is out of range')
       print('1<=data input<=3')
    else:
         # Convert list to array numpy zeros and ones
         # The print func,in next 3 lines is no required is used for improve
         # output
         print(36*"*")
         print(12*' ' + 'ouput:' + 12*' ')
         print('')
         print('zero array:')
         print(np.zeros(L,int))
         print('')
         print('ones array:')
         print(np.ones(L,int))



