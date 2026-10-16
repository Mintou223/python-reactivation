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
    indexation(tensions25)

    # slicing de la liste des tensions
    slicing(tensions25)

    # test du piège de la vue sur ndarray
    view_trap(tensions25)

    # Affichage tensions en surcharge
    surcharge(tensions25, rekk)

    # 2D array et axis
    circuits_2d()


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
              "Une comparaison seraient non exploitable\n")


def indexation(tensions):
    '''Affichage d'éléments à différents index'''
    print("Eléments de tensions:\n"
          f"1er élément:{tensions[0]}, dernier élément :{tensions[-1]}, "
          f"3e élément:{tensions[2]}\n")


def slicing(tensions):
    '''Slicing de la liste des tensions '''
    print(f"Les 5 premières tensions: {tensions[:5]}\n"
          f"Toutes les tensions à partir de 6 V: {tensions[tensions >= 6]}\n"
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


# boolean mask
def surcharge(tensions, rekk):
    '''Calcul et affichage de la 1ère tension en surcharge;
    usage d'un masque booléen.'''
    puissances = (tensions**2)/rekk
    masque_surcharge = puissances > 0.125
    cpt = np.count_nonzero(masque_surcharge)
    print(f"Masque pour puissances supérieures à 0.125W:\n {masque_surcharge}")
    print(masque_surcharge.shape, masque_surcharge.dtype)
    print(f"Il y a {cpt} tensions en surcharge.")

    puissances_surcharge = puissances[masque_surcharge]
    tensions_surcharge = tensions[masque_surcharge]

    print(f"Première tension en surcharge: "
          f"{tensions_surcharge[0]}V --> {puissances_surcharge[0]:.6f}W\n")


# 2D et axis
def circuits_2d():
    """Calcul (et vérification) simplifié des résistances
     équivalentes pour plusieurs circuits en une fois."""
    circ_2d = np.array([[100, 220, 330, 470],
                        [130, 250, 360, 500],
                        [160, 280, 390, 530]], dtype=float)
    rekk_serie = circ_2d.sum(axis=1)
    rekk_serie_other_axis = circ_2d.sum(axis=0)
    rekk_parallel = 1/np.sum(1/circ_2d, axis=1)
    print(f"Les {circ_2d.shape[0]} circuits:\n{circ_2d}")
    print(f"Forme (lignes, colonnes): {circ_2d.shape}")
    print(f"Nombre de dimensions: {circ_2d.ndim}")
    print(f"Nombre total d'éléments: {circ_2d.size}")
    print(f"Type de données: {circ_2d.dtype}")
    print(f"La résistance R3 du circuit 2: {circ_2d[1, 2]}")
    print(f"Le circuit 2 en entier: {circ_2d[1]}")
    print(f"La résistance R1 de chaque circuit: {circ_2d[:, 0]}")
    print(f"Résistances équivalentes - circuits en série: {rekk_serie}")
    print(f"rekk on other axis - circuits en série: {rekk_serie_other_axis}")
    print(f"Résistances équivalentes - circuits en parallèle: {rekk_parallel}")
    print(f"R_eq est toujours inférieure à la plus petite résistance "
          f"du circuit: {np.all(circ_2d.min(axis=1) > rekk_parallel)}\n")


if __name__ == "__main__":
    main()
