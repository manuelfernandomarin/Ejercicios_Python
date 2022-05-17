#-------------------------------------------------------------------------------
# Name: Diagonal_Difference        module1
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

def diagonalDifference(arr1):
    # Define a empty list called ma to store values of main diagonal
    ma = []
    # Define a empty list called sec to store values of secondary diagonal
    sec = []
    # Define process to obtain main diagonal: a[1][1];a[2][2];a[3][3];...a[n][n]
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            if i==j:
               ma.append(arr1[i][j])
            else:
                 pass
    # Define process to obtain secondary diagonal: a[1][n]; a[2][n-1]; a[3][n-2]
    # ... a[n][1]
    # Define initial values to counters:
    hh = len(arr1)-1
    tr = 0
    # Loop to obtains elements from array arr1:
    for _ in range(len(arr1)):
        sec.append(arr1[hh][tr])
        hh = hh-1
        tr = tr+1
    # Obtain the sum of list elements
    s1 = sum(ma)
    s2 = sum(sec)
    diffabs= abs(s1-s2)
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
    # invoke function diagonalDifference(w)
    result = diagonalDifference(arr)
    # The next 3 print func, is no required is used for improve output
    print(36*"*")
    print(12*' ' + 'ouput:' + 12*' ')
    print('')
    print(result)
