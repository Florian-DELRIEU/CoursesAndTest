import os # Module de commande systeme
import pickle # Module d'enregistrement

os.chdir("/Users/floriandelrieu/Desktop")
mon_fichier = open("Fichier_Test.txt","r") # w:write r:read a:append

contenu = mon_fichier.read()
print(contenu)

mon_fichier.close()

mon_fichier = open("Fichier_Test.txt","w")
mon_fichier.write("Ceci est un test")
del contenu

mon_fichier.close()
mon_fichier = open("Fichier_Test.txt","r")
print("------------------------------------------------------------")
contenu = mon_fichier.read()
print("------------------------------------------------------------")
print(contenu)
mon_fichier.close()
del contenu 
del mon_fichier

print("------------------------------------------------------------")
print("------------------------------------------------------------")

with open("fichier_test.txt","r") as mon_fichier:
    texte = mon_fichier.read()

if mon_fichier.closed == True:
    print("fichier fermé")
os.chdir("/Users/floriandelrieu/OneDrive/Cours/Python/Tutos")