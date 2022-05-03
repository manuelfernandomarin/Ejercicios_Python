#-------------------------------------------------------------------------------
# Name: Tuples       module1
# Purpose: Given an integer, n and n space-separated integers as input, create
# a tuple, t, of those n integers. Then compute and print the result of hash(t)
# Note: hash() is one the functions in the _ _builts_ _ module, so it need not
# be imported.
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))

