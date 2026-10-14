'''Pratique de la vectorization avec numpy.'''


import sys
import time
import numpy as np
from circuit import lire_circuit


def main():
    """Fonction principale contenant la logique globale du script."""
    chemin = "data/circuit.txt"
    try:
        u, resistances = lire_circuit(chemin)
    except FileNotFoundError:
        print("Erreur: Le fichier n'existe pas.")
        sys.exit(1)
    except ValueError as e:
        print(f"Erreur: {e}")
        sys.exit(1)

    n = 1_000_000
    r = np.array(list(resistances.values()))
    rekk = r.sum()  # circuit série
    tensions = np.linspace(0, u, n)
    tensions25 = np.linspace(0, u, 25)

    # comparaison boucle for VS vectorisation
    comparaison_time(tensions, rekk)

    # exécution de l'indexation
    indexation(tensions25, rekk)

    # slicing de la liste des tensions
    slicing(tensions25)

    # test du piège de la vue sur ndarray
    view_trap(tensions25)


def comparaison_time(tensions, rekk):
    '''Comparaison des temps d'exécution
    boucle for et méthode vectorisée sur un même calcul.'''
    # Version boucle for
    courant_for = []
    powers_for = []
    debut_for = time.perf_counter()
    for v in tensions:
        i = v/rekk
        courant_for.append(i)
        powers_for.append(i*v)
    duree_for = time.perf_counter() - debut_for

    # Version vectorisée
    debut_vect = time.perf_counter()
    courant_vect = tensions/rekk
    powers_vect = courant_vect * tensions
    duree_vect = time.perf_counter() - debut_vect
    rapport_duree = duree_vect/duree_for

    if np.allclose(powers_for, powers_vect):
        print(f"Les résultats de puissance sont identiques.")
        if rapport_duree < 1:
            print(f"La vectorisation dure le moins longtemps.\n"
                  f"Rapport for/vect : {duree_for/duree_vect}\n"
                  f"vect: {duree_vect:.6f} vs for: {duree_for:.6f}\n")
        elif rapport_duree > 1:
            print(f"La boucle for dure le moins longtemps: "
                  f"Rapport vect/for : {duree_vect/duree_for}\n"
                  f"vect: {duree_vect:.6f} vs for: {duree_for:.6f}\n")

    else:
        print("Les résultats de puissance ne se ressemblent pas. "
              "Une comparaison seraient impertinente")


def indexation(tensions, rekk):
    '''Affichage d'éléments à différents index'''
    powers = (tensions**2)/rekk
    print("Eléments de tensions:\n"
          f"1er élément:{tensions[0]}, dernier élément :{tensions[-1]}, "
          f"3e élément:{tensions[2]}\n")


def slicing(tensions):
    '''Slicing de la liste des tensions '''
    print(f"Les 5 premières tensions: {tensions[:5]}\n"
          f"Toutes les tensions à partir de 6 V: {tensions[12:]}\n"
          f"Une tension sur deux: {tensions[::2]}\n")


# VIEW TRAP
def view_trap(tensions):
    '''experimentation du piège de modification d'une view'''
    tensions = tensions.copy()
    print(f"L'originale:\n {tensions}")
    tranche = tensions[:13].copy()
    tranche += 100
    print(f"tensions après modification protégée de la slice:\n {tensions}")
    tranche_trap = tensions[:13]
    tranche_trap += 100
    print(f"tensions après modification non protégée "
          f"de la slice:\n {tensions}\n")


if __name__ == "__main__":
    main()
