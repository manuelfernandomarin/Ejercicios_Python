#-------------------------------------------------------------------------------
# Name: Find Angle MBC       module1
# Purpose: ABC is a right triangle 90º degrres at B. Therefore, segment AB and
# BC in point B = 90ª. The Point M is the mid point of hypotenuse AC. You are
# given the lenghts AB and BC.
# Your task is to find angle called theta, in triangle MBC, this angle are
# betwen segment MB and BC in degree.
# Input Format: The first line contains the lenght of side AB.
# The scond line contains the lenght of side BC.
# Contrains 0< AB <= 100      0< BC <= 100  Lengths AB an BC are natural numbers
# Output Format: output angle MBC in degress, Round angle to nearest integer.
#
# Author:      tioFer
#
# Created:     23/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
# The code must to define given two dimension of right triangle at point
# B,the first data input is length of side AB, second data input is length
# of side BC. The code have to calculate angle called theta of triangle MBC
# where point M es the midpoint of hypotenuse AC
import math
AB=int(input()) # User's data input
BC=int(input()) # User's data input
HYPOT=math.hypot(AB,BC)
# Calculate the required angle in degrees
angle=round(math.degrees(math.acos(BC/HYPOT)))
degree=chr(176) # for use the degree symbol
# The print func,in the next 3 lines is no required is used for improve output
print(36*"*")
print(12*' ' + 'ouput:' + 12*' ')
print('')
print(angle,degree,sep='')