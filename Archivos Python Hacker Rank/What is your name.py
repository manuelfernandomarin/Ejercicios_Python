#-------------------------------------------------------------------------------
# Name: What is your name        module1
# Purpose: You are given thefirstname and lastname of a person on two different
# lines. Your tassk is to read them and print the following sentence:
# 'Hello firetname latname! You just delved into python'
# Function description: print_full_name has the following parameters:
# ° type string, first: firstname;  ° type string last: lastname
# Prints ° string: "Hello firstname lastname!You just delved into python" where
# firstname and lastname are replaced with first and last
# Input Format: The first line contains the first name, and the second line
# contains the last name.
# Constrains: length of the first name, and last name are aeach <= 10.
#
# Author:      tioFer
#
# Created:     29/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def print_full_name(first,last):
    return print('Hello '+ first +' '+ last +'! You just delved into python.')


if __name__ == '__main__':
   # With the function str(), the user's data input is forced ot be string type
   first_name = str(input())
   last_name = str(input())
   # use conditional function to verify that data input are the length of
   # firstname and last name are each <= 10
   if len(first_name) > 10 or len(last_name) > 10 :
      print('The length of firstname is :'+ str(len(first_name)) +
      ' length of last name is '+ str(len(last_name)))
      print('Because the string length < 10'  )
      sys.exit('input data out of range')
   else:
       pass
   # The next 3 print func, is no required is used for improve output
   print(36*"*")
   print(12*' ' + 'ouput:' + 12*' ')
   print('')
   print_full_name(first_name, last_name)




