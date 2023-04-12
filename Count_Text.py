TextInput = input('Entrez votre texte ici: ');
assert type(TextInput) == str
ListeMots = TextInput.split(" ");

Invent = dict();

for mot in ListeMots:
    mot = mot.lower()
    
    for lettre in mot:

        NewVarName = lettre
        Invent[NewVarName] = 0

for mot in ListeMots:
    mot = mot.lower()
    
    for lettre in mot:

        NewVarName = lettre
        Invent[NewVarName] += 1

print(Invent)