#https://www.codingame.com/training/easy/create-the-longest-sequence-of-1s

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

b = input()
b = b.split("0")
maxi = 0
for i in range(1,len(b)):
    temp = len(b[i-1]) + len(b[i])
    if(temp > maxi):
        maxi = temp
print(maxi + 1)
