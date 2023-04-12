def set_var(newvalue):
	"""
	Teste la portée des variables
	
	Dans cette fonction "var" est définie localement et est donc détruits à la 		fin de la function
	"""
	
	try:
		print("La variable valait: {}.".format(var))
	
	except NameError:
		print("La variable n'existais pas")
		
	var = newvalue
	
	print("Maintenant, la variable vaut: {}".format(var))
	
def ajouter( liste , valeur_a_ajouter ):
	"""
	Ajoute un élément à la liste alors que la liste est externe à la fonction
	"""
	liste.append(valeur_a_ajouter)
	
def modifier_liste(liste):
	"""
	La liste n'est pas modififé car la valeur de "liste" est supprimé après la 		fonction
	"""
	liste = ["a","1"]
	
	
	
