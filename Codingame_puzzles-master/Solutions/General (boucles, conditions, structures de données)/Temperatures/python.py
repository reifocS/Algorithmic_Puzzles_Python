import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526
# must find the one that is the closest to zero
if len(temps) == 0:
    print("0")
else:
    temps_split = list(map(int,temps.split()))
    temp2=([abs(x) for x in temps_split])
    if(min(temp2)) in temps_split:
        res=min(temp2)
    else:
        res=-min(temp2)
print(res)
