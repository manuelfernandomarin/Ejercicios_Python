#-------------------------------------------------------------------------------
# Name: String Split and Join        module1
# Purpose: Given a string. Split the string on a " " (space) delimeter and join
# using a - hypen.
# Function Description: Complete the split_and_join function in the editor below
# split_and_join has the following parameters: ° string line: a string-separate
# of space-separate words.
# Returns ° string: the resulting string
#
# Author:      tioFer
#
# Created:     28/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def split_and_join(line ) :
    # Convert the user' data input (string) to a list of characters string
    g = line.split(" ")
    # Use method join to iterable type to obtain a chracter string
    return "-".join(g)


if __name__ == '__main__':
   # Use a str function to convert the user's data input to a string type
   line = str(input())
   # The next print func, is no required is used for improve output
   print(36*"*")
   print(12*' ' + 'ouput:' + 12*' ')
   print('')
   result = split_and_join(line )
   print(result)
