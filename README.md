# python-reactivation

Ce dépôt contient des exercices de réactivation de Python, autour de circuits électriques en série.

## Installation

```
python -m venv .venv
.venv/Scripts/activate
python -m pip install -r requirements.txt
```

## Exercices

- `exercices/01_resistances.py` : calcul de la résistance équivalente en série et en parallèle.
- `exercices/02_puissances.py` : calcul de puissances reçues par les résistances.
- `exercices/03_lecture_circuit.py` : calcul de puissances reçues par des résistances extraites d'un fichier txt.
- `exercices/04_circuit_modulaire.py` et `exercices/circuit.py` : même travail que le point précédent, le script affiche les résultats et intercepte les erreurs.
- `exercices/05_numpy.py` :familiarisation avec la bibliothèque numpy

## Exercice 04 : module et script

Le module contient toutes les fonctions dont aura besoin le script, et toutes les erreurs sont interceptées et gérées sans traceback.

Lancement depuis la racine du dépôt :

```
python exercices\04_circuit_modulaire.py
```

### Fichiers de test

- `data/circuit.txt` : contient les valeurs valides.
- `data/circuit_sans_egal.txt` : contient une ligne sans symbole '='.
- `data/circuit_sans_tension.txt` : ne contient aucune ligne définissant la tension U.
- `data/circuit_resistance_nulle.txt` : contient une résistance nulle.
- `data/circuit_tension_negative.txt` : contient une tension négative.
- `data/circuit_valeur_non_numerique.txt` : contient une valeur non-numérique.
- `data/circuit_double_egal.txt` : contient deux '=' sur la même ligne.

## Exercice 05 — Premiers pas avec numpy (`05_numpy.py`)

**Objectif** : Familiarisation avec la bibliothèque numpy via l'utilisation d'outils de vectorisation, d'indexation, et de calculs sur des objets multidimensionnels.

### Contenu

| Fonction | Notion numpy | Ce qu'elle montre |
|---|---|---|
| `comparaison_time` | Vectorisation (*vectorization*) | Comparaison des temps d'exécution boucle for VS méthode vectorisée sur le calcul du courant et de la puissance reçue par les résistances d'un circuit. |
| `indexation` | Indexation (*indexing*) | Affichage du 1er, 3e et dernier élément d'un ndarray contenant les tensions des résistances du circuit. |
| `slicing` | Tranches (*slicing*) et sélection par valeur | Affichage de différentes tranches de tensions selon différents critères (>=6V, 5 premières tensions, etc.). |
| `view_trap` | Vue et copie (*view* / *copy*) | Démonstration du piège de manipuler directement les vues d'un ndarray plutôt qu'une copie; parade en intégrant la méthode copy() en début de fonction lorsqu'on écrit dans le ndarray (en cas de simple lecture pas besoin de la méthode copy()). |
| `surcharge` | Masque booléen (*boolean mask*) | Identification rapide des puissances dépassant un certain seuil et report de cette règle sur la liste des tensions afin d'identifier facilement les tensions de surcharge. |
| `circuits_2d` | Tableaux 2D et paramètre `axis` | Calcul (et vérification) simplifié des résistances équivalentes pour plusieurs circuits en une fois. |

### Lancement

À exécuter depuis la racine du dépôt :

    source .venv/Scripts/activate
    pip install -r requirements.txt
    python exercices/05_numpy.py

> Fonctionnement du script : dossier courant + chemin relatif = endroit réellement cherché
donc le script doit être lancé depuis la racine du dépôt pour lire ses données dans data/circuit.txt (un chemin relatif).

### Résultats clés

- **Vectorisation** : méthode vectorisée 31, 34, 42, 54, 57, 63, 81, 91 et 188 fois plus rapide que la boucle for; l'écart peut changer selon l'allocation de ressources du processeur de l'ordinateur selon les sollicitations: temps de déclenchement, priorité accordée à la tâche, engorgement, etc.
- **Surcharge** : Premier dépassement à 10V au lieu du 9.94V théorique, car 10V est la première valeur "dépassante" que la précision de notre array (pas de 0.5V) nous permet de lire.
- **Circuits 2D** : calcul de la résistance série (1120 Ω) et parallèle (50,75 Ω) du premier circuit, et contrôle physique effectué avec R_eq_parallèle < min(résistances du circuit).
