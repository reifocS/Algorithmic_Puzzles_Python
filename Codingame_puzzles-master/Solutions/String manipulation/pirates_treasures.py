#link https://www.codingame.com/training/easy/pirates-treasure

import sys
import math
import itertools
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def neighbours_of(i, j):
    """Positions of neighbours (includes out of bounds but excludes cell itself)."""
    neighbours = list(itertools.product(range(i-1, i+2), range(j-1, j+2)))
    neighbours.remove((i, j))
    return neighbours

w = int(input())
h = int(input())
matrix = [] 
for i in range(h):
    matrix.append(input().split())

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j]=int(matrix[i][j]) 
for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                if matrix[i][j]!=0:
                    continue
                obstacles=[]
                a=neighbours_of(i,j)
                for e in a:
                    if e[0] >=h or e[0]<0:
                        continue
                    if e[1]>=w or e[1]<0:
                        continue
                    obstacles.append(matrix[e[0]][e[1]])
                if 0 in obstacles:
                    continue
                print (j,i)

