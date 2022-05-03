#-------------------------------------------------------------------------------
# Name: Validating postal Codes        module1
# Purpose: A valid postal code P have to fullfil both below requirements:
# 1. P must be a number in the range from 100000 to 999999 inclusive.
# 2. P must not contain more than one alternating repetitive digit pair.
# Alternating repetitive digits are digits wich repeat inmediately after the
# next digit. In other words, an internating repetitive digit pair is formed by
# two equal digits that have just a single digit between them.
# Your task is provide two regular expressions regex_in_range and
# regex_alternating_repetitive_digit_pair. Where:
# regext_integer_in-range should match only integers range from 100000 to 999999
# inclusive regex_alternating_repetitive_digit_pair  should find alternating
# repetitive digits pairs in a given string.
# Both these regular expressions will be used by the provided code template to
# check if the input string P is a valid postal code using:
# (bool(re.match(regex_integer_in_range, p)) and
# len(re.findall(regex_alternating_repetitive_digit_pair. p)) < 2)
# Input Format: Locked stub code in the editor reads a single string denoting P
# from stdin and uses provided expression and your regular expressions to
# validate if P is a valid postal code.
# Output Format: You are not responsible for printing anything to stdout. locked
# stub code in the editor does that.
#
# Author:      tioFer
#
# Created:     23/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# The regex expressions lines 31 & 32 el writer of progam must to fill r"------"
# blank spaces
regex_integer_in_range = r"\b([1-9]\d{5})\b"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

import re
P = input()
# The print func,in lines 38-40 is no required is used for improve output
print(36*"*")
print(12*' ' + 'ouput:' + 12*' ')
print('')
print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)