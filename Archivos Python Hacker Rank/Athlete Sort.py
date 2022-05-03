#-------------------------------------------------------------------------------
# Name: Athlete Sort       module1
# Purpose: You You are given a spreadsheet that contains a list of N athletes
# and their datails (such as age, height, weight and so on). You are required
# to sort the data based on the Kth attribute and print the resulting table.
# Note: that K is indexed from 0 to M-1, where M is the number of attribtes.
# Note: If two attributes are the same for different row, for example, if two
# two athletes are of same age, print the row that appeared first in the input.
# Input format: The first line contains N and M separated by a space.
# The next N lines each contain M M elements. The last line contains K.
# Contrains 1<=N, M<=1000; 0<=K<=M. Each element <= 1000.
# Output Format: Print N lines of sorted table. Each line should contain the
# space separated elements.
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # assign user's data input to vars n(nunber athletes) and m(numbers
    # of attributes)
    n,m=list(map(int,input().split()))
    # assign to a list all records for attributes for every athlete
    data=[list(map(int,input().split())) for _ in range(n)]
    # assign the user's input data for k attribute to sort
    k=int(input())
    # Add print function to optimizing output (this in not required
    print(35*'*')
    print("List sorted based in k^th attribute" )
    print(14*' ','output',15*' ')
    # process to sort data
    data.sort(key=lambda x:x[k])
    for i in data:
        print(*i)




