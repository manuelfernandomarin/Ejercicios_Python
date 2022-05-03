#-------------------------------------------------------------------------------
# Name: Miniuon Game        module1
# Purpose: Define the winnwr in the game. Give a String two player use the same
# String, make words uno using word that start with wovel, the other palyer
# with consonant.
#
# Author:      tioFer
#
# Created:     19/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def minion_game(string):
    # Due that look for sbstring  in a word of length n. Therefore, since
    # any substring start exclisively with either consonants or wovwel,  only
    # need to count the number of substring starting with a wovel and substract
    # from the total number of substrings to get the number of substrings
    # starting with consonants, or vice versa.
    #
    slen=len(string)
    sub=sum(slen-i for i in range(slen))
    kev=sum(slen-i for i in range(slen) if string[i] in 'AEIOU')
    s=sub-kev

    if s>kev:
        print(f"Stuart {s}")
    elif s<kev:
        print(f"Kevin {kev}")
    else: print("Draw")



if __name__ == '__main__':
   s=input()
   minion_game(s)
