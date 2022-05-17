#-------------------------------------------------------------------------------
# Name: Mini-Max_Sum      module1
# Purpose: Given five positiva integer, find the minimum and maximum values
# taht can be calculated by summing exactly four of five integers. Then print
# print the respective minimum ans maximum values as a single line of two-sepa-
# rated long integers.
# Example: arr = [1,3,5,7,9] the minimum sum is: 1+3+5+7=16 and the maximum sum
# is: 3+5+7+9=24. The function prints:
#*******************************************
#   16  24
#*******************************************
#
# Function Description: Complete the miniMaxSum function in the editor below.
# miniMaxSum has the following parameter(s): ° arr: an array of 5 integers
# Print: Print two space-separated integers on one line: the minimum sum and the
# maximum sum of 4 of 5 elements.
# Input Format: a single line of five space-separated integers
# Constrains: 1 <= arr[i] <= 10e9
# Output Format: Print two space-separated long integers denoting the respective
# minimum and maximum values that can be calculated by asumming exactly four of
# five integer. (The output can be greater than a 32 bit integer.)
#
#
# Author:      tioFer
#
# Created:     15/05/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def miniMaxSum(arr1):
    # Process to calculate the sum of 4 of 5 elements of array provided by user
    # for i in range(len(arr1)), using a list for compression:

    sumarr=[sum(arr1)-arr1[i] for i in range(len((arr1)))]

    mimsum, maxsum = min(sumarr), max(sumarr)

    print(mimsum, maxsum)



if __name__ == '__main__':

   arr = list(map(int, input().rstrip().split()))
   # Verify if each element in list provided by users is in the
   # range 1 <= arr[i] <= 10e9
   for s in range(len(arr)):
       if arr[s] < 1 or arr[s] > pow(10,9):
          print("The element a[i] index",s,"of array ",arr[s],"is out of range")
          sys.exit('input data out of range: 1 <= a[i] <= 10e9')
       else: pass


   # The next 3 print func, is no required is used for improve output
   print(36*"*")
   print(12*' ' + 'ouput:' + 12*' ')
   print('')

   arr

   miniMaxSum(arr)
