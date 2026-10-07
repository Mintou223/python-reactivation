'''Lecture d'un circuit série depuis un fichier texte.'''

with open('data/circuit.txt', 'r') as f:
    resistances={}
    for ligne in f:
        nom, valeur=ligne.split('=')
        nom = nom.strip()
        valeur=float(valeur)
        if nom=='U':
            u=valeur
        else:
            resistances[nom]=valeur

print(f"U = {u} V")
print(resistances)
p={P: (R*u**2/sum(resistances.values())**2)*1000 for P,R in resistances.items()}#calcul de la puissance reçue par chaque résistance en mW
print(p)
