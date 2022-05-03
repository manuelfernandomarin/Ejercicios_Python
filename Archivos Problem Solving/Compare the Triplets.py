#-------------------------------------------------------------------------------
# Name:Compare the Triplets        module1
# Purpose: Given two list givem by the useer, compare every element a[i] & b[i],
# if a[i] > b[i] give a point to owners of list a; if a[i] < b[i] give a point
# to ownwer to list b, finally if a[i] = b[i] give one point two both owners of
# list a and b. Return a array whit score od two owner's list a and b, where the
# first element od array is the final score of ownwer list a, the second element
# is final score of owner list b.
#
# Author:      tioFer
#
# Created:     03/05/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import os
import random
import re
import sys
# ****************************************************************************
# Complete the 'compareTriplets' function below
#*****************************************************************************
#
# The function is expected to return an ITEGER_ARRAY.
# The function accepts following parameters:
# 1. INTEGER_ARRAY a
# 2. INTEGER_ARRAY b
#*****************************************************************************

def compareTriplets(la, lb):
    # Write your code
    # define a Array with final score and elemets elema and elemb that store
    # the final scrore for every owner's list (list a and list b)
    arrfinal = []
    elema, elemb = 0, 0
    # Define new function to compare elements and assing values
    for k in range(len(la)) :
        # call function 'evalueterecord' to compare elemtens with same index in
        # lists
        s, r = evaluaterecord(la[k],lb[k])
        # Define counters to every comparision for elemets of eeach list
        elema += s
        elemb += r
    arrfinal.append(elema)
    arrfinal.append(elemb)
    # return el array with final score
    return arrfinal

# Define function that eveluate every item en each list
def evaluaterecord(o,p):
    ito, itp = 0,0
    if o > p:
       ito = 1
    elif o < p:
         itp = 1
    elif o == p :
         pass

    return ito, itp




if __name__ == '__main__':
   #ftr = open(os.environ['OUTPUT_PATH'], 'w')

   a = list(map(int, input().rstrip().split()))

   b = list(map(int, input().rstrip().split()))

   result = compareTriplets(a, b)
   # added
   print(result)




