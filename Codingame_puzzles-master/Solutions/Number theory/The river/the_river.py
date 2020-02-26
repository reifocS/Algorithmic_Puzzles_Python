def follow (x):
    return x + sum (int (c) for c in str (x))

i = int(input())
j=[int(i) for i in str(i)]
leng=len(j)
maxi=leng*9
answer="NO"

for element in range(1,maxi+1):
    precedent=i-element
    if precedent<0:
        break
    elif follow(precedent)==i:
        answer='YES'
        break
print(answer)