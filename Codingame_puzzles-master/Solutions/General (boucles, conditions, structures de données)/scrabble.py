#https://www.codingame.com/training/medium/scrabble

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
words=[]
for i in range(n):
    w = input()
    words.append(w)
letters = list(input())

scrbl={1:"eaionrtlsu",2:"dg",3:"bcmp",4:"fhvwy",5:'k',8:"jx",10:"qz"}
scrabble={lettre:k for k,v in scrbl.items() for lettre in v }
current_max=None
max_index=None
def isvalid(mot):
    letters_copy=letters.copy()
    for lettre in mot:
        if lettre not in letters_copy:
            return False
        letters_copy.remove(lettre)
    return True
for index,word in enumerate(words):
    if isvalid(word):
        if current_max==None:
             current_max=sum(scrabble[c] for c in word)
             max_index=index
        max_point=sum(scrabble[c] for c in word)
        if max_point>current_max:
            current_max=max_point
            max_index=index

        
print(words[max_index])
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
