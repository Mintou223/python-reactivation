'''Lecture d'un circuit série depuis un fichier texte.'''
import math

import pip

# extraction des données des résistances depuis un fichier texte
with open('data/circuit.txt', 'r') as f:
    resistances = {}
    for ligne in f:
        nom, valeur = ligne.split('=')
        nom = nom.strip()
        valeur = float(valeur)
        if nom == 'U':
            tension = valeur
        else:
            resistances[nom] = valeur

print(f"U = {tension} V")
print(resistances)

# calcul des puissances
r_eq = sum(resistances.values())  # circuit en série
courant = tension/r_eq  # circuit en série
# calcul de la puissance reçue par chaque résistance en mW
powers = {p: (r*courant**2) for p, r in resistances.items()}
for k, v in powers.items():
    n = resistances[k]
    print(f"{k}: {n} \u03A9 --> {v*1000:.2f} mW")
plus_sollicite = max(powers, key=powers.get)
print(f"La résistance qui reçoit le plus de puissance est: {plus_sollicite}")

# vérification de la loi de conservation de l'énergie
if math.isclose(tension*courant, sum(powers.values())):
    print("La loi de conservation de l'énergie est vérifiée")
else:
    print("La loi de conservation de l'énergie n'est pas vérifiée ou il y a une erreur dans le calcul des puissances")
