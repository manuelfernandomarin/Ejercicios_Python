#-------------------------------------------------------------------------------
# Name: String Validators       module1
# Purpose: You are given a string S. Your task is to find out if the string S
# contains: alphanumerics characters, aiphabetical characters, digits,
# lowercase, and uppercase character
# Input Format: A single line containing a string S. Constrains: 0<len(S)<1000
# Output Format: In the first line, print True if S has any alphanumerics
# character. Otherwise, print False. In the second line, print True if S has any
# alphabetical characters. Otherwise print False. In the third line, print True
# true if S has any digits. Otherwise print False. In the fourth line, print
# True if S has any lowercase characters. Otherwise print False. In the fifth
# line, print True if S has any uppercase characters. Otherwise print False.
#
# Author:      tioFer
#
# Created:     29/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

if __name__ == '__main__':
    s = input()
    # Use function str() to ensure that variable has type string
    s = str(s)
    # Verify that user's data input string length is in range
    if len(s) < 0 or len(s) > 1000 :
       print('The length of string S ',len(s),+' is out limit')
       sys.exit('input data out of range 0<len(S)<1000')
    # The next 3 print func, is no required is used for improve output
    print(36*"*")
    print(12*' ' + 'ouput:' + 12*' ')
    print('')
    # Create an iterable format in this case tupla the methods called tt to
    # evaluate the string
    tt = ('isalnum','isalpha','isdigit','islower','isupper')
    # Using a nested for methods to scannner all the string to evaluate each
    # character of the string, The the for function into the print function is
    # used to scan every chacter of the string. The external for function is
    # used to iterate the evaluation method applied to each character
    for i in tt:
        print('The string contains any'+i+' '+str(any(eval('c.'+i+'()')
        for c in s)))














