#-------------------------------------------------------------------------------
# Name: Find a string       module1
# Purpose: The user enters a string and substring. The algorithn have to print
# the number of times that the substring occurs in the  given string.
# String transversal will take place from left to right, not from to left.
# Note: String letters are case-sensitive.
# Input Format: The first line
#
# Author:      tioFer
#
# Created:     29/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def count_substring(string, sub_string):
    # Defining a counter and is setup to zero
    count1 = 0
    # Using for function to scan al lenght of string. In the function range
    # is added 1 (+1) to include the all elenments in range
    for i in range(len(string)-len(sub_string)+1):
        # Use a condicional if to evaluate if segments of string == sub_string
        if(string[i:i+len(sub_string)] == sub_string):
                                       count1 += 1
        else: pass
    return count1

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
