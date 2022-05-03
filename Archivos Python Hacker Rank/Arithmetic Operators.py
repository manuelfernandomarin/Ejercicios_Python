#-------------------------------------------------------------------------------
# Name: Arithmetic Operators        module1
# Purpose: The provided code stub reads two integers a and b. Add code to print
# three code to print three lines where:
# 1. El first line contains the sum of two numbers.
# 2. Tge second line contains the difference of two numbers (first-second).
# 3. The third line contains the product of the two numbers
# Note: Input: the firs line constains the first integer, the second line
# contains the second integer
#
# Author:      tioFer
#
# Created:     21/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    a = int(input())
    b = int(input())
if a < 1 or a > pow(10,10):
    print("The number b is out of range")
    print("1 <= a <= pow(10,10)")
else:
    if b < 1 or b > pow(10,10):
        print("The number b is out of range")
        print("1 <= b <= pow(10,10)")
    else:
        suma = a+b
        diferencia = a-b
        producto = a*b
        print(suma)
        print(diferencia)
        print(producto)




