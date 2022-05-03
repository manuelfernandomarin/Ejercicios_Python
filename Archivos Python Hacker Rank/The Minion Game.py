#-------------------------------------------------------------------------------
# Name: The Minion Game       module1
# Purpose:Kevin and Stuart want to play the 'The Minion Game'
# Game Rules: Both players are given the same string S. Both players have to
# make substrings using the letters of the string S.
# Stuart has to make words satrting with consanants. Kevin has to make words
# starting with vowels. The game ends when both players have made all possible
# substrings.
# Scoring: A player gets +1 point for each occurrence of the substring in the
# string S. Scoring: A player gets +1 point for each occurrence of the string S.
# For Example: string S = BANANA ; Kevin's vowel beginning word ANA. Here, ANA
# ANA occurs twice in BANANA. Hence, kevin will get 2 points.
# Your task is to determine the winner of the game and their score.
# Function Description: Complete the minion_game in editor below.
# minion_game has the following parameters:* string string: the string to
# analize .
# Prints: * string: the winner's name and score, separated by a space on one
# line, or Draw if there is no winner.
# Input Format: A single line of input containning the string S.
# Note: The string S will contain only uppercase letters: |A-Z|.
# Constraints 0<len(S)<= 10^6
#
# Author:      tioFer
#
# Created:     24/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def minion_game(string):
    # your code goes here
    slen=len(string)
    sub=sum(slen-i for i in range(slen))
    kev=sum(slen-i for i in range(slen) if string[i] in 'AEIOU')
    s=sub-kev

    if s>kev:
        print(f"Stuart {s}")
    elif s<kev:
        print(f"Kevin {kev}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    # Add print function to optimizing output (this in not required
    print(35*'*')
    print("Winner player and score" )
    print(14*' ','output',15*' ')
    minion_game(s) # Invoque the function minion_game(string