"""Module contenant les fonctions qui renvoient :
- la tension et le dictionnaire des résistances
- la résistance équivalente d'un circuit en série
- le courant dans le circuit
- la puissance reçue par chaque résistance"""


def lire_circuit(chemin):
    """Lit le fichier de données et
    retourne la tension et le dictionnaire des résistances."""

    tension = None
    resistances = {}
    with open(chemin, 'r') as f:
        for numero, ligne in enumerate(f, start=1):
            ligne = ligne.strip()
            if not ligne or ligne.startswith('#'):
                continue
            if "=" not in ligne:
                raise ValueError(f"La ligne {numero} ne contient pas "
                                 f"de '=': {ligne}")
            nom, valeur = ligne.split('=')
            nom = nom.strip()
            valeur = valeur.strip()
            try:
                valeur = float(valeur)
            except ValueError as e:
                raise ValueError(f"La ligne {numero} contient "
                                 f"une valeur non numérique: {valeur}") from e
            if nom == 'U':
                if valeur <= 0:
                    raise ValueError(f"La ligne {numero} contient une tension "
                                     f"négative ou nulle: {valeur}V")
                tension = valeur
            else:
                if valeur <= 0:
                    raise ValueError(
                        f"La ligne {numero} contient "
                        f"une résistance négative ou nulle: {valeur}Ω")
                resistances[nom] = valeur
    if tension is None:
        raise ValueError("La tension n'a pas été spécifiée dans le fichier.")
    return tension, resistances


def resistance_equivalente(resistances):
    """Calcule la résistance équivalente d'un circuit en série."""
    return sum(resistances.values())


def courant(tension, r_eq):
    """Calcule le courant dans le circuit."""
    return tension / r_eq


def puissances(resistances, i):
    """Calcule la puissance reçue par chaque résistance."""
    return {nom: (r * i**2) for nom, r in resistances.items()}
