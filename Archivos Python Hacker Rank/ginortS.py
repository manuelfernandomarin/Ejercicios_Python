#-------------------------------------------------------------------------------
# Name: ginortS       module1
# Purpose: You are given strin S. S contains alphanumeric characters only.
# Your task is to sort the sting in the following manner:
# * All sorted lowercase letters are ahead of uppercase letters
# * All sorted uppercase letters are ahead of digits
# * All sorted odd digits are ahead of even digits
# Input Format: A single line of input contains the string S.
# Constrains 0<len(S) < 1000
# Ouput Formats: Output the sorted String S.
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# Enter your code here. Read input from STDIN. Print output to STDOUT
# Storing alphanuemric user's data input
S=input()
# get the lower, upper, odd, even type of user's data unput
lower=sorted([s for s in S if s.isalpha() and s.islower()])
upper=sorted([u for u in S if u.isalpha() and u.isupper()])
odd=sorted([o for o in S if not o.isalpha() and int(o)%2 == 1])
even=sorted([e for e in S if not e.isalpha() and int(e)%2 == 0])
# Release results
print(''.join(lower+upper+odd+even))
