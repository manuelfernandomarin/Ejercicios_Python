#-------------------------------------------------------------------------------
# Name: Pyhon Evaluation        module1
# Purpose: The eval()  expression is a very powerful built-in function of
# Python. It helps in evaluating an expression. The expression can be a Python
# statement, or code object.
# Task You are given an expression in a line. Read that line as a string
# variable,  such as var, and print the result using eval(var).
# Constraint input string is less than 100 chearacters
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
v=str(input()) # convert espresion to string type the user's data input
# Process to verify that string expresion meet the constrain <= 100 characters
if len(v) > 100:
    print ('The input string > 100 characters')
else:
    eval(v) # evaluate v
