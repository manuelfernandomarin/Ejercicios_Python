#-------------------------------------------------------------------------------
# Name: if-else       module1
# Purpose: Given an integer nurical value, n, perform the next following
# conditional actions:
# º if n is odd print Weird º if n is even and the inclusive range 2 o 5, print
# Not Weird º if n is even and in the inclusive range 6 to 20 print Weird
# º if n is even and greater than 20, print Not Weird
#
# Author:      tioFer
#
# Created:     21/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import os
import random
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if n < 1 or n > 100:
    print("The input number must to be on inclusive range 1 to 00")
else:
    if n % 2 != 0:
        print("Weird")
    else:
        if n >= 2 and n <= 5 :
            print("Not Weird")
        else:
            if n >= 6 and n <= 20 :
                print("Weird")
            else:
                if n > 20 :
                    print("Not Weird")

