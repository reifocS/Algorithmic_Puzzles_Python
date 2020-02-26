
#link to puzzle https://www.codingame.com/training/easy/rectangle-partition


import sys
import math
from collections import defaultdict
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def permutation(X, d):
    length = len(X)
    for i in range(len(X)):
        for j in range(i + 1,len(X)):
            d[abs(X[j]-X[i])] += 1
    return X
w, h, count_x, count_y = [int(i) for i in input().split()]
x = defaultdict(int)
y = defaultdict(int)
for i in input().split():
    k = int(i)
    x[k] += 1
for i in input().split():
    k = int(i)
    y[k] += 1
x[w] += 1
y[h] += 1
permutation(list(x),x)
permutation(list(y),y)
total = 0
for _ in x:
    if _ in y:
        total += x[_]*y[_]
print(total)
