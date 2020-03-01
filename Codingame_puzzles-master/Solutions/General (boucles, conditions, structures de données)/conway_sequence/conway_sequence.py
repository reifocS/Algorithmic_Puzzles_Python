# In mathematics, the look-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...
# This programs output the chosen line of the sequence 

def next_sequence(line):
    actual = line[0]
    cpt = 0
    nextOne = []
    for i in line:
        if i == actual:
            cpt +=1
        else:
            nextOne.append(str(cpt)+actual)
            actual = i
            cpt = 1
    nextOne.append(str(cpt)+actual)
    return "".join(nextOne)

n = int(input())
for i in range(n):
    l = next_sequence(l)
print(l)
