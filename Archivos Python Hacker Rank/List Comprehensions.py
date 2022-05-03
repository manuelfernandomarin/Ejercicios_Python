#-------------------------------------------------------------------------------
# Name: List Comprehensions       module1
# Purpose: User's data are three integer values x,y, and z, representing the
# dimensions of a cube along with an integer n. Print a list of all possible
# coordinates given by (i,j,k) on 3D grid where the sum of i+j+k is not equal
# to n. Here 0<=i<=x; 0<=j<=y; 0<=k<=z. Use a list comprehensions rather than
# multiples loops, as a learning exercise
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    # Store user's data input in vars x y z and n
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # Creating a list for every axe
    listx = [i for i in range(x + 1)]
    listy = [j for j in range(y + 1)]
    listz = [k for k in range(z + 1)]
    # Creating a list with tridimensional points and x1+y1+z1 != n
    listcoordinates = [[x1,y1,z1] for x1 in listx for y1 in listy
    for z1 in listz if x1 + y1 + z1 != n ]
    print(listcoordinates)



