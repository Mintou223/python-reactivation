'''Lecture d'un circuit série depuis un fichier texte.'''
import math
import sys

chemin = 'data/circuit.txt'
# extraction des données des résistances depuis un fichier texte
try:
    with open(chemin, 'r') as f:
        resistances = {}
        tension = None
        for numero, ligne in enumerate(f, start=1):
            ligne = ligne.strip()
            if ligne.startswith('#') or ligne == '':
                continue
            if '=' not in ligne:
                print(f"Le fichier contient une ligne invalide "
                      f"sur la ligne {numero}: {ligne}.")
                sys.exit(1)
            nom, valeur = ligne.split('=')
            nom = nom.strip()
            try:
                valeur = float(valeur)
            except ValueError:
                print(f"Le fichier contient une valeur non numérique "
                      f"sur la ligne {numero}: {ligne}.")
                sys.exit(1)
            if nom == 'U':
                if valeur <= 0:
                    print(f"Valeur de tension négative ou nulle "
                          f"sur la ligne {numero}: {ligne}.")
                    sys.exit(1)
                else:
                    tension = valeur
            else:
                if valeur <= 0:
                    print(f"Valeur de résistance négative ou nulle "
                          f"sur la ligne {numero}: {ligne}.")
                    sys.exit(1)
                resistances[nom] = valeur
except FileNotFoundError:
    print("Erreur : Le fichier n'existe pas.")
    sys.exit(1)

if tension is None:
    print("Erreur : La tension n'a pas été définie dans le fichier.")
    sys.exit(1)

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
puissance_theorique = tension*courant
puissance_totale = sum(puissances.values())
if math.isclose(puissance_theorique, puissance_totale):
    print("La loi de conservation de l'énergie est vérifiée")
else:
    print("La loi de conservation de l'énergie n'est pas vérifiée "
          "ou il y a une erreur dans le calcul des puissances")
