#-------------------------------------------------------------------------------
# Name: Find Angle       module1
# Purpose: Calculate angle called theta.
#
# Author:      tioFer
#
# Created:     18/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
    # The code must to define given two diemsions of right triangle at point
    # B, the firts data input is length of side AB, second data input is length
    # of side BC. The code have to calculate angle called theta of triangle MBC
    # where point M is the midpoint od hypotenuse AC. Since M is the midpoint of
    # hypotenuse, then it divided the triangle into two similar isosceles
    # triangles such that AM=MC=BM, This implies that angle at point C is equak
    # to angle theta

    import math
    AB=int(input()) # User's data input
    BC=int(input()) # User's data input
    HYPOT=math.hypot(AB,BC)
    # Calculate the require angle in degrees
    angle=round(math.degrees(math.acos(BC/HYPOT)))
    degree=chr(176) # for use the degree symbol
    print(angle,degree,sep='')


