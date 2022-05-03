#-------------------------------------------------------------------------------
# Name: Find the Runner Up Score        module1
# Purpose: Given the participant's score sheet for your University Sport Day,
# you are required to find the runner-up score. You are given n score.
# Store them in a list and find the score of the runner-up.
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


if __name__ == '__main__':
    n = int(input())  # Store the user's data input number of scores
    # Process create a Map object (user's input data are assigned to array
    # for every score
    arr = map(int, input().split())
    # Convert Map to list of unique items
    arr_set = list(set(arr))
    arr_set.sort()
    arr_set.reverse() # --> Sort items plus reverse order
    # This print is not required, is only for improve the answer presentation
    print("Second higest Score:")
    print(len("Second higest Score:")*"*")
    print(arr_set[1]) # --> Print second higest number

    # ***************Note:**************************************
    # In this example the index of every element of list arr_set is the record
    # of every stundet




