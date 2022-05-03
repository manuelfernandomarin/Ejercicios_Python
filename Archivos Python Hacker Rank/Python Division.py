#-------------------------------------------------------------------------------
# Name:Python Division        module1
# Purpose: Given two Integers values from STDIN. The code will do mathematics
# operation a) The integer division using oerator "//" this will be the first
# output line. b) Made the floating division using operator "/" y will be the
# second line in output line
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    a = int(input())  # Store the first user data input
    b = int(input())  # Store the second user data input
    # Developing the two divisions operations and output results
    valorentero = a // b
    valorflotante = a / b
    print(valorentero)
    print(valorflotante)

