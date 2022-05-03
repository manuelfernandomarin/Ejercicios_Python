#-------------------------------------------------------------------------------
# Name: Swap Case        module1
# Purpose: You are given a string and your task is swap cases. In other words,
# convert all lowrcase letters to uppercse letters and vice versa.
# Example:  Python 3 ---> pYTHON 3
# Complete the function called swap_case in the editor. The function has the
# next parameters: * string: the string to modify. This function wiil be return
# * string: the modified string. The input format: A single line containing a
# string called s. Constrains 0<len(s)<= 1000
#
# Author:      tioFer
#
# Created:     23/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def swap_case(s) :
    return s.swapcase()

# the function defined up lines called swap_case() use the build in function
# swapcase() where s is a data type string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    # The print func,in lines 27-30 is no required is used for improve output
    print(36*"*")
    print(12*' ' + 'ouput:' + 12*' ')
    print('')
    print(result)
