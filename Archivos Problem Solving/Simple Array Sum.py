#-------------------------------------------------------------------------------
# Name: Simple Array Sum       module1
# Purpose: Given an array of integers, find the sum of its elements. For example
# if array ar= [1,2,3] ,the sum of elements of array 1+2+3 = 6, so return 6.
# Function Description: Complete the simpleArraySum function in the editor
# below. It must return the sum of the array elements as an integer. The
# funntion simpleArraySum has the following parameters(s):
# ° ar: an array of integers
# Input Format: The first line contains an integer, n, denoting the size of
# array. The second line contains n space-separated integers representing the
# array's elements. Constrains: 0< n, ar[i] <= 1000.
# Output Format: Print the sum of array's elements are a single integer.
#
# Author:      tioFer
#
# Created:     24/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    return sum(ar)

if __name__ == '__main__':
   # delete fptr: fptr = open(os.environ['OUTPUT_PATH'], 'w')
   # because return a error

   ar_count = int(input().strip())

   ar = list(map(int, input().rstrip().split()))

   result = simpleArraySum(ar)
   # Add print function to optimizing output (this in not required
   print(35*'*')
   print('The sum of array elemets is:')
   print(14*' ','output',15*' ')
   print(result)

   # delete fptr.write: fptr.write(str(result) + '\n') see comemnt line 39


   # delete fptr.close() see comemnt line 39

   # In the ejcution of this code, the function on module os retun a error
   # that is the reason that is deleted and is labeled in paragraphs above
   # the commands on os module, belong to original code provoded by HackerRank
