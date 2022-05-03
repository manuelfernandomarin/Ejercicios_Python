#-------------------------------------------------------------------------------
# Name: Cloudy Day       module1
# Purpose: Complete the function maximumPeople which takes four arrays
# representing the populations of each town, locations of the towns, locations
# of the clouds, and the extents of coverage of the clouds respectively, and
# returns the maximum number of people that will be in a sunny town after
# removing exactly one cloud
#
# Author:      tioFer
#
# Created:     26/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import os
import random
import re
import sys
#
# Complete the maximumPeople function below
#
# The function us expected to return a LONG_INTEGER.
# The function accepts following parameters:
# LONG_INTEGER:ARRAY to next parameters:
# 1. p; 2. x, 3. y, 4. r
#

# Funtion maximumPeople Return the maximum number of people that will be in a
# sunny twon after remove exactly one cloud.

def maximumPeople(p, x, y, r) :
    # Define a empty dictionary and empty list
    one_covered_cloud = {}
    sort_list = []

    # Loop add to distance r of cloud ends decimal value 0.9 taken position of
    # clouds on axe y where is define the start place and end place of cloud
    for i in range(0,len(y)) :
        sort_list.append((y[i]-r[i], i, -1)) # start place
        sort_list.append((y[i]+r[i] + 0.9, i, -2)) # end place

    # Loop add to city position x the decimal vale 0.5
    for i in range(0,len(p)) :
        sort_list.append((x[i] + 0.5, -1, i)) # city point

    # Sort ordered by cloud's start, town, and cloud's end
    sort_list = sorted(sort_list, key=lambda x:x[0])

    # Defining storage containers
    covered_cloud = set()
    sunny_population = 0
    max_one_covered = 0

    # Using Loops to fill containers
    for x, cloud_index, town_index in sort_list :
        if town_index == -1 : # Cloud start place
           covered_cloud.add(cloud_index)
        elif town_index == -2 :  # Cloud end place
             covered_cloud.remove(cloud_index)
        else: # this is town
              if len(covered_cloud ) == 0 :
                 sunny_population += p[town_index]
              elif len(covered_cloud) == 1:
                   for a in covered_cloud :
                       one_covered_cloud[a] = one_covered_cloud.get(a,0) + p[town_index]
                       max_one_covered = max(max_one_covered,one_covered_cloud[a])
    return sunny_population + max_one_covered



if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()




