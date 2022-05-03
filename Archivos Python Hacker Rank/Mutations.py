#-------------------------------------------------------------------------------
# Name: Mutations      module1
# Purpose: Read a given string, change the character at a given index and then
# print the modified string.
# Function description: Complete the mutate_string function in the editor below.
# mutate_string has the following parameters:ª stringstring the string to change
# ª int position: the index to insert the character at
# ª string character: the character to insert
# Returns ª string: the altered string
# Input Format: The first line contains a string, string. The next line contains
# an integer position, the index location and a string character, separated by
# a space.
#
# Author:      tioFer
#
# Created:     29/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def mutate_string(string, position, character):
    # Convert a list the user's data input string
    l = list(string)
    # Due that parameter position is type string, this will be convert o integer
    position = int(position)
    # Process to exchange the caracter in list index given by integer position
    # and replce by user data input given in the character type data
    l[position] = character
    # Process to convert list to string using method ''.join(list)
    string_mod = ''.join(l)

    return string_mod

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    # The next 3 print func, is no required is used for improve output
    print(36*"*")
    print(12*' ' + 'ouput:' + 12*' ')
    print('')
    s_new = mutate_string(s, int(i), c)
    print(s_new)
