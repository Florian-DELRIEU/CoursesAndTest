var1 = "bonjour"
var2 = " AUrevoir"
assert (type(var1) and type(var2)) == str
print(var1 + " ou " + var2)
print("Quand on dit {0}, on répond {1}." .format(var1.capitalize() \
      , var2.capitalize()) )
print("Mais on pourrai dire aussi: " + var1.upper() + \
      ". Généralement c'est plus poli.")
print(" Si je te dis {} tu me dis {}".format(var1,var2) + \
      " Alors que tu pourrais me dire {0} non ?".format(var2))

nom = "Delrieu"
prenom = "florian"
age = 21
assert type(age) == ( int or float )
age = str(age)
assert (type(nom) and type(prenom)) == str
print("Je suis {} {}".format(nom,prenom))
print(" On peut préciser mon age" + \
      "({age} ans) suivie de mon nom: {nom}".format(nom="Dupont",age="22") )

#
#
mot = "bac"
print(mot)
mot = "s" + mot[1:]
print(mot)

print("----------------------------------------------------------------")
print("----------------------------------------------------------------")
print("----------------------------------------------------------------")

print(" J'ecris un message \n sur plusieurs lignes ")

print(" Je peux aussi ecrire \n" \
      " comme ça"
      )
