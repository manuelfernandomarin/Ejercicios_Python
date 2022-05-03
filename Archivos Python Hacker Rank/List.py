#-------------------------------------------------------------------------------
# Name: List       module1
# Purpose:Consider a list (list = []). You can perform the following commands:

# 1. insert i e: Insert integer e at position i
# 2. print : Print the list
# 3. remove e: Delete the first occurrennce of integer e
# 4. append e: Insert integer e at the end of the list
# 5. sort: Sort the list.
# 6. pop : Pop the last element from the list.
# 7. reverse: Reverse the list.
# Initialize your list and read in the value of followed by n lines of
# commands where each command will be of the 7 types listed above.
# Iterate through each command in order and perform the corresponding
# operation on your list.
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


if __name__ == '__main__':
    N = int(input()) # Define like integer value the number of elements
    l = [] # Setup an empty list called 'l' to store all data given for user's
    cdm = [] # Setup an empty list to store the commands to be used in list 'l'
    # process to input data user's to lists called 'l'
    for t in range(N):
        x = input().split(" ")
        l.append(x)
    # execute the commands to be used in list
    for i in range(len(l)):
        if l[i][0] == 'insert':
            x = int(l[i][1])
            y = int(l[i][2])
            cdm.insert(x,y)
        elif l[i][0] == 'print' :
            print(cdm)
        elif l[i][0] == 'remove' :
            cdm.remove(int(l[i][1]))
        elif l[i][0] == 'append' :
            cdm.append(int(l[i][1]))
        elif l[i][0] == 'sort' :
            cdm.sort()
        elif l[i][0] == 'pop' :
            cdm.pop()
        elif l[i][0] == 'reverse' :
            cdm.reverse()




