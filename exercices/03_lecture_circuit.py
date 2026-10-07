'''Lecture d'un circuit série depuis un fichier texte.'''
import math

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
courant = tension/r_eq
# calcul de la puissance reçue par chaque résistance en W
puissances = {nom: (r*courant**2) for nom, r in resistances.items()}
for nom, puissance in puissances.items():
    r = resistances[nom]
    print(f"{nom}: {r} \u03A9 --> {puissance*1000:.2f} mW")
plus_sollicite = max(puissances, key=puissances.get)
print(f"La résistance qui reçoit le plus de puissance est: {plus_sollicite}")

# vérification de la loi de conservation de l'énergie
if math.isclose(tension*courant, sum(puissances.values())):
    print("La loi de conservation de l'énergie est vérifiée")
else:
    print("La loi de conservation de l'énergie n'est pas vérifiée "
          "ou il y a une erreur dans le calcul des puissances")
