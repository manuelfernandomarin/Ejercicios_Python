#-------------------------------------------------------------------------------
# Name: Staircase       module1
# Purpose: A staircase of size n its base and height are both equal to n. It is
# drawn using # symbols and spaces. The last line is not preceded by any spaces.
# Write a program that prints a staircase  of size n.
# Function Description: Complete the staircase function in the editor below.
# staircase has the following parameter(s): ª int n an integer
# Print: Print a staircase as descrite above.
# Input Format: A single integer, n, denoting the size of the staircase.
# Constrain: 0 < n < = 100.
# Output: Ptint a staircase of size n using # symbols and spaces.
# Note: The last line must have 0 spaces in it.
#
# Author:      tioFer
#
# Created:     15/05/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def starircase(n1):
    for i in range(1, n1+1):
        print(("#"*i).rjust(n1))

if __name__ == '__main__':
    n = int(input().strip())
    # Verify if n parameter is in range 0 < n <= 100
    if n <= 0 or n > 100:
       print('The number n of elements of matrix  ',n,' is out limit')
       sys.exit('input data out of range: 0 < n <= 100')
    else: pass

    # The next 3 print func, is no required is used for improve output
    print(36*"*")
    print(12*' ' + 'ouput:' + 12*' ')
    print('')

    starircase(n)
