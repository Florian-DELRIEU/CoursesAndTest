chaine = input("Entrez la phrase que vous voulez écrire en verlan :")
length = len(chaine)
verlan = str()
i = 1
assert type(chaine) == str
assert (type(length) and type(i))  == ( int or float )
assert type(verlan) == str

while i <= len(chaine):
    x = chaine[- i]
    verlan = verlan + str(x)
    i += 1

print(verlan)