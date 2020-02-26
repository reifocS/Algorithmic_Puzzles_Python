#https://www.codingame.com/ide/puzzle/order-of-succession

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class person:
    def __init__(self,name,parent,birth,death,religion,gender):
        self.name=name
        self.parent=parent
        self.birth=birth
        self.death=death
        self.religion=religion
        self.gender=gender
        
    def child(objet):
        child=[]
        for n in Personne:
            if n.parent==objet.name:
                child.append(n.name)
        return child
        
personne=[]
n = int(input())
for i in range(n):
    name, parent, birth, death, religion, gender = input().split()
    personne.append(person(name,parent,int(birth),death,religion,gender))

Personne=sorted(personne, key=lambda person: person.birth)
Personne=sorted(personne, key=lambda person: person.gender, reverse=True)

for n in Personne:
    if n.parent=='-':
        start= (n.name)
        
def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path
    

graphe={}
for n in Personne:
    graphe[n.name]= (person.child(n))
    
def isdead(liste):
    dead_ppl=[]
    for n in liste:
        if n.death!='-' or n.religion=='Catholic':
            dead_ppl.append(n.name)
    return dead_ppl
dead=isdead(Personne) 
mypath=dfs_recursive(graphe,start)
mypath2=[n for n in mypath if n not in dead]   
print(*mypath2,sep="\n")  
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

