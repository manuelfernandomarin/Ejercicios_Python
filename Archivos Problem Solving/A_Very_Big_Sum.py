#-------------------------------------------------------------------------------
# Name: A_Very_Big_Sum       module1
# Purpose: Calculate and print the sum of the elements in an array, keeping in
# in mind that some of those integer may be quite large. Complete the function
# aVeryBigSum in the editor below. It must return the sum of all array elements
# the function has the following parameter(s):
# ° long:the sum of all array elements.
# Input Format: The first line of the input consist of a integer n.
# The next line contains n space-separated integers contained in the array.
# Output Format: Return the integer sum of the elements in the array.
# Constrains: 1 <= n <= 10 ;  0 <= ar[i] <= 10 exp10
#
# Author:      tioFer
#
# Created:     14/05/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def aVeryBigSum(ar):
    # Note: in Python 3, do not exist any more the long number, like Python 2
    s = sum(ar)
    return print(s)

if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int,input().rstrip().split()))
    # The next 3 print func, is no required is used for improve output
    print(36*"*")
    print(12*' ' + 'ouput:' + 12*' ')
    print('')
    result = aVeryBigSum(ar)
