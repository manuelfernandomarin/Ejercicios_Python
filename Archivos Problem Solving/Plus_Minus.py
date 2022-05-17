#-------------------------------------------------------------------------------
# Name: Plus_Minus       module1
# Purpose: Given an array of integers, calculate the ratios of its elements that
# are positive, negative and zero. Print the value of ecah fraction on a new
# line with six decimal. Note: This challange introduces precision probblems.
# The tst cases are scaled to six decimal places, though answers with absolute
# error of up to 10 e-4 are acceptable.
# Example: arr = [1,1,0,-1,-1]. There are n=5 are 5 elements, two positive, two
# negative, and one zero. Consider the number total de of positive numbers,
# negatives numbers, and the total of zeros in the list provided. In this case
# have n = 5 (total of elements on list), p = 2 (two positive values), neg = 2
# (two negative values), and z = 1 (one zero value), consider that ratio = p/n;
# ratio = neg/n, and ratio = z/n; that is 2/5 = 0.400000; 2/5 = 0.400000;
# 1/5 = 0.200000. The resulta are printed as:
#*********************************************************
#** 0.400000
#** 0.400000
#** 0.200000
#*********************************************************
#
# Function Description: Complete the plusMinus function in the editor below.
# This function has the following parameter(s): ° int arr[n] of integers
# Print the ratios  of positive, negative and zero values in the array. Each
# value should be printed on a separate line with 6 digits after the decinal
# point The function should not return a value.
# Input Format: The first line contains an integer, n, the size of the array.
# The second line contains n space-separated integers that describe arr[n].
# Constrains: 0 < n <= 100; -100 <= arr[i] <= 100
# Output Format: Print the following 2 lines, each to 6 decimals:
#
# Line 1 proportion positive ratio value
# Line 2 proportion negative ratio value
# Line 3 proportion zero ratio value
#
# Author:      tioFer
#
# Created:     15/05/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def plusMinus(arr1):
    # Get the ratio of total elements of positive, negative and zero values from
    # array provodes by user
    ps = (len([x for x in arr1 if x > 0])) / n
    neg = (len([y for y in arr1 if y < 0])) /n
    zr = (len([z for z in arr1 if z == 0])) /n
    # Process to print results
    print(format(ps, '.6f'))
    print(format(neg, '.6f'))
    print(format(zr, '.6f'))


if __name__ == '__main__':
   n = int(input().strip())

   arr = list(map(int, input().rstrip().split()))

   # The next 3 print func, is no required is used for improve output
   print(36*"*")
   print(12*' ' + 'ouput:' + 12*' ')
   print('')

   plusMinus(arr)

