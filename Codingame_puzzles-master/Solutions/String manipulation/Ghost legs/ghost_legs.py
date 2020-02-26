#https://www.codingame.com/training/easy/ghost-legs

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


grille=[]
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()
    grille.append(line)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

depart=[]
for idx,_ in enumerate(grille[0]):
    if _ !=' ':
        depart.append((0,idx))


for s in depart:
    x,y=s
    top= grille[x][y]
    while x<len(grille)-1:
        x+=1
        if y+1<w and grille[x][y+1]=='-':
            y+=3
        elif y-1>=0 and grille[x][y-1]=='-': 
            y-=3

    print(top+grille[x][y])
