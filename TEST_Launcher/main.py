import donnees
import run

case = donnees.Case1  #Chargement des donnees
case["a"] = 100  # Modifications si besoin

run.loop(case)