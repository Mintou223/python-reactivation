# python-reactivation

Ce dépôt contient des exercices de réactivation de Python, autour de circuits électriques en série.

## Installation

```
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Exercices

- `exercices/01_resistances.py` : calcul de la résistance équivalente en série et en parallèle.
- `exercices/02_puissances.py` : calcul de puissances reçues par les résistances.
- `exercices/03_lecture_circuit.py` : calcul puissances par résistances extraites d'un fichier.
- `exercices/04_circuit_modulaire.py` et `exercices/circuit.py` : même travail que le point précédent, le script affiche les résultats et intercepte les erreurs.

## Exercice 04 : module et script

Le module contient toutes les fonctions dont aura besoin le script, et toutes les erreurs sont gérées sans traceback.

Lancement depuis la racine du dépôt :

```
python exercices\04_circuit_modulaire.py
```

### Fichiers de test

- `data/circuit.txt` :contient les valeurs valides.
- `data/circuit_sans_egal.txt` :contient une ligne sans symbole '='.
- `data/circuit_sans_tension.txt` : ne contient aucune ligne définissant la tension U.
- `data/circuit_resistance_nulle.txt` : contient une résistance nulle.
- `data/circuit_tension_negative.txt` : contient une tension négative.
- `data/circuit_valeur_non_numerique.txt` : contient une valeur non-numérique.
