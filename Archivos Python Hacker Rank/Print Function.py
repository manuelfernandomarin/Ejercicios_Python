#-------------------------------------------------------------------------------
# Name: Print Function        module1
# Purpose: The include code stub will read an integer, m, from STDIN. Without
# using any string methods, try to print the following:
# 123···n
# Note that "···" represents the consecutive values between.
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


if __name__ == '__main__':
    n = int(input())  # Assign to variable n the user's data input
    # Process to define if user's data input in range 1<=n<=150
    if n < 1 or n > 150 :
        print("el valor numerico: ",n, " esta fuera de rango")
        print("El rango de los valores es 1<=n<=150")
    else:
        # recursive proces to print conscutive values 1 to n
        for i in range(1, n+1) :
            print(i, end='')




