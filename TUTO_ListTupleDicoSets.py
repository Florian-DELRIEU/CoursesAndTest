import numpy as np
"""
DICO: {key:value} or DICO[key] = value
    - if data should be modified and need key : value association
    
LIST: [value1,value2] or List(structure)
    - simple collection that can be modified
    
SET: {value1,value2} or set(structure)
    - if you dont want doublons and specific order
    
TUPLE: (value1,value2)
    - if data cannot be changed
"""

# List
liste1 = list()
liste2 = [1,2,3]
assert(type(liste1) == list and type(liste2) == list)
liste1 = ["a",2,2.2]
i = 0
while i < 3:
    current = liste1[i]
    print(current)
    print("i=",i)
    i += 1

del liste2
liste2 = list()

i = 0
while i < 10:
    liste2.insert(i,i)
    i += 1
    
liste3 = list()
liste3 += liste2

A = np.linspace(1,10,10)

C = [1,2,3,4]
for c in C:
    c = c*10
    

#----------------------------------------------------------------------------
dico = dict()
a = list()

l = ["a","b",]
c = [1,2]

dico["1"] = l.copy()
dico["2"] = c

l.clear()

print(dico)

#---------------------- SETS
a = {1, 2, 4, 1, 6, 5, 3, 4}
b = {1, 2, 7, 9, 8, 5, 3, 6}
print(a)  # duplicate are not showed and show in order
print(a | b)  # show (a AND b)
print(a & b)  # show in(a and b)
print(a - b)  # in a but not in b
print(b - a)  # in b but not in a
print(a ^ b)  # in a OR in b only