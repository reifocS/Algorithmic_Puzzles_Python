import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def happy_number(nb):
    memory = []
    result = nb
    while(result != "1"):
        s = 0
        for _ in range(len(result)):
            s += pow(int((result[_])),2)
        result = str(s)
        if(result in memory):
            return nb + " :("
        memory.append(result)
    return nb + " :)"
n = int(input())
for i in range(n):
    x = input()
    print(happy_number(x))

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

