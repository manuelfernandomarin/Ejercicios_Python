#-------------------------------------------------------------------------------
# Name: Loops        module1
# Purpose: Write Python code that read a integer, n, from STDIN. For all non-
# negative integers i < n. Print i**2 or i*i
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    n = int(input())
    print(15*'*') # print functions in lines 15 & 16 is not required in orinal
    print('', sep='\n') # code, only to show i**2 values, after data input

    if n < 1 or n > 20:
        print("The integer value : ", n, ", is out of range")
        print("Range is: 1<=n<=20")

    # Recursion procedure to calculate square value of each integer
    else:
        k = 0  # Establish initial value to counter to zero
        # Recursion procedure (loop) to calculate the square value of every integer
        while k < n :
            p = k * k
            print(p)
            k = k + 1



