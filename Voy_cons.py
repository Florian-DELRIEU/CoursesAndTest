
chaine = input("Entrez votre phrase: ")
lettre = str()
voyelle = str()
consonne = str()
symb = str()
number = str()
other = str()
count_voyelle = int()
count_consonne = int()
count_symb = int()
count_space = int()
count_number = int()
count_other = int()

assert type(chaine) == str

for lettre in chaine:
    lettre = lettre.lower()
    if lettre in "aeiouyèàîêâïäë":
        count_voyelle += 1
        voyelle += lettre
    elif lettre in ",?;.:/!§*%^¨$£=+°()[{}]":
        count_symb += 1
        symb += lettre
    elif lettre in "1234567890":
        number += lettre
        count_number += 1
    elif lettre == " ":
        count_space += 1
    elif lettre in "zrtpqsdfghjklmwxcvbn":
        consonne += lettre
        count_consonne += 1
    else:
        other += lettre
        count_other += 1

print("Le texte est composé de:")
print("   - {} voyelles".format(count_voyelle))
print("   - {} consonnes".format(count_consonne))
print("   - {} symboles".format(count_symb))
print("   - {} espaces".format(count_space))
print("   - {} nombres".format(count_number))