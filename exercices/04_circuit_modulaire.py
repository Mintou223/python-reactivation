"""Script d'exécution du module circuit.py"""
import math
import sys
from circuit import lire_circuit, resistance_equivalente, courant, puissances


def main():
    """Fonction principale contenant la logique globale du script."""

    chemin = "data/circuit.txt"
    try:
        u, res = lire_circuit(chemin)
    except FileNotFoundError:
        print("Erreur: Le fichier n'existe pas.")
        sys.exit(1)
    except ValueError as e:
        print(f"Erreur: {e}")
        sys.exit(1)
    r_eq = resistance_equivalente(res)
    i = courant(u, r_eq)
    power = puissances(res, i)

    print(f"U = {u} V")
    for nom, r in res.items():
        print(f"{nom}: {r} Ω")
    print(f"Résistance équivalente: {r_eq} Ω")
    print(f"Courant : {i*1000:.2f} mA")
    for nom, v in power.items():
        print(f"{nom}: {res[nom]} Ω --> {v*1000:.2f} mW")

    most_powered = max(power, key=power.get)
    print(f"La résistance qui reçoit le plus de puissance est: {most_powered}")

    p_total = sum(power.values())
    p_th = u * i
    if math.isclose(p_total, p_th, rel_tol=1e-9):
        print(f"La loi de conservation de l'énergie est vérifiée: "
              f"{p_total:.6f} W = {p_th:.6f} W")
    else:
        print(f"La loi de conservation de l'énergie n'est pas vérifiée "
              f"ou il y a une erreur de calcul: {p_total} W != {p_th} W")


if __name__ == "__main__":
    main()
