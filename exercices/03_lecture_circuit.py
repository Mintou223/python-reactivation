'''Lecture d'un circuit série depuis un fichier texte.'''
import math

#extraction des données des résistances depuis un fichier texte
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

print(f"U={u} V")
print(resistances)

#calcul des puissances 
r_eq=sum(resistances.values())#circuit en série
I=u/r_eq #circuit en série
#calcul de la puissance reçue par chaque résistance en mW
powers={p: (r*I**2) for p,r in resistances.items()}
for k, v in powers.items():
    n=resistances[k]
    print(f"{k}: {n} \u03A9 --> {v*1000:.2f} mW")
print(f"La résistance qui reçoit le plus de puissance est: {max(powers, key=powers.get)}")
#vérification de la loi de conservation de l'énergie
if math.isclose(u*I,sum(powers.values())):
    print("La loi de conservation de l'énergie est vérifiée")
else :
    print("La loi de conservation de l'énergie n'est pas vérifiée ou il y a une erreur dans le calcul des puissances")
