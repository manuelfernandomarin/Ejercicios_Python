#-------------------------------------------------------------------------------
# Name: Find a string Regex       module1
# Purpose: The user enters a string and substring. The algorithn have to print
# the number of times that the substring occurs in the  given string.
# String transversal will take place from left to right, not from to left.
# Note: String letters are case-sensitive.
# Input Format: The first line
#
# Note: in this case use library re (regular expresion)
# Author:      tioFer
#
# Created:     29/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re

def count_substring(string, sub_string):
    # Employ regular espresion function findall()
    reg_exp = '(?='+sub_string+')'
    return len(re.findall(reg_exp, string))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    # The next 3 print func, is no required is used for improve output
    print(36*"*")
    print(12*' ' + 'ouput:' + 12*' ')
    print('')
    # Invoque function
    count = count_substring(string, sub_string)
    print('The number of ocurrences of: ' + sub_string +' is:' )
    print(count)
