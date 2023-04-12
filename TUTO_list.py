liste = list()
liste = [1, 2, 5]
assert type(liste) == list
print("J'affiche 'liste'")
print(liste)
liste[2] = 3
print("Je remplace 5 par 3")
print(liste)
print("Je rajoute une chaine")
liste = liste + ["c'est le lol"]
print(liste)
print("-------------------------")

LISTE = ["C'est une liste" , "Qui contient un liste" , liste]
print(LISTE)
print("---------------------")


var = 2
print("var = {}".format(var))
del var;

liste.remove(2)
print("Supprime le 2 dans [liste]" )
print(liste)
liste.insert(1,2)
print(liste)

print("-------------------------")
print("-------------------------")
print("-------------------------")
del liste; del LISTE;

liste = ["a","b","c","d","e","f"]
for i in liste :
    print(i)
    
for i,elt in enumerate(liste):
    print("A l'indice {} se trouve la lettre {}".format(i,elt))

liste = [[1,2,"a"],[3,4,"b"],[5,6,"c"]]
for i,j,lettre in liste:
    print("On a {} et {} on a {}".format(i,j,lettre) )

print("-------------------------")
print("-------------------------")
print("-------------------------")
del liste; del elt; del i; del j; del lettre;

tuple_vide = ();
type(tuple_vide) is tuple 
assert (2,) != (2)
del tuple_vide;
tuple1 = (1,2,3,)
a,b,c = tuple1
liste = [1,2,3]
d,e,f = liste
assert (a==d and b==e and c==f)

chaine = "Bonjour a toi"
liste_chaine1 = chaine.split(" ")
liste_chaine2 = chaine.split("a")
del chaine
chaine = "a".join(liste_chaine1)

print(" --------------------------------------------------- ")
print(" --------------------------------------------------- ")

def function_list(*parametres):
    print("j'ai reçu : {}".format(parametres))
function_list("b")


