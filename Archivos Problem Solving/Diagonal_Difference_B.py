#-------------------------------------------------------------------------------
# Name: Diagonal_Difference_B        module1
# Purpose: Given a square matrix, calculate the absolute difference between the
# the sums of main diagonal and secundary diagonal.
# Function description: Complete the diagonalDifference function in the editor
# below. This function takes the following parameter: ° int arr[n][m]: an array
# of integers.
# Return: ° int:the absolute diagonal difference
# Input Format: The first line contains a single integer, n, the number of rows
# and columns in the square matrix called arr. Each of the next n lines
# describes a row, arr[i], and consists of n space-separated integers arr[i][j].
# Constrains: ° -100<= arr[i][j] <= 100
# Output Format: Return the absolute difference the sums of the matrix main
# diagonal and secondary diagonal as a integer.
#
# Author:      tioFer
#
# Created:     15/05/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def diagonalDifference(arr1):
    # Define process to obtain main diagonal: a[1][1];a[2][2];a[3][3];...a[n][n]
    # and process to obtain secondary diagonal: a[1][n]; a[2][n-1]; a[3][n-2]
    # ... a[n][1]
    diffabs = abs(sum(arr1[i][i]-arr1[i][-1-i] for i in range(len(arr1))))
    return diffabs


if __name__ == '__main__':
    # Process to obtain data user
    # Request input data of row n and column n of square matrix
    n = int(input().strip())
    # Define an empty list to store users data input of row elemets
    arr = []
    # Process request user data input of rows of squere matrix
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    # Verify if matix elements are out of range
    outval = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] < -100 or arr[i][j] > 100:
               outval.append(arr[i][j])
            else: pass
    if len(outval) > 0:
       rr = outval
       print('The next elements of matrix  ',rr,' are out limit')
       sys.exit('input data out of range: -100 <= a[i][j] <= 100')
    # invoke function diagonalDifference(w)
    result = diagonalDifference(arr)
    # The next 3 print func, is no required is used for improve output
    print(36*"*")
    print(12*' ' + 'ouput:' + 12*' ')
    print('')
    print(result)
