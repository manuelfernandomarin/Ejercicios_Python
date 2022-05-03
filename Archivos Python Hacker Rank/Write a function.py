#-------------------------------------------------------------------------------
# Name: Write a function       module1
# Purpose: Given a year, determine wheter it is a leap year. If it is a leap
# year, return the Boolean True, otherwise  return false. Note that the code
# stub provided reads from STDIN and passes arguments to the is_leap function.
# It is only necesary to complete the is_leap function
#
# Author:      tioFer
#
# Created:     22/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

if __name__ == '__main__':

    def is_leap(year):
        leap = False  # Assing boolean value False to leap variable
        # Conditional loop to verify is year provided by user's is in limits
        if year < 1900 or year > pow(10,5) :
            print("The year: ", year, " is out of range")
            print("The range is 1900<=year<=pow(10,5)")
        else:
            # Procedure to define leap year
            if year % 400 == 0 or (4 == 0 and year % 100 != 0) :
                return not leap
            else:
                pass
        return leap

    # Process to recieve user's data input annd invoque function is_leap(year)
    year = int(input())
    print(is_leap(year))





