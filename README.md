# python-reactivation

Ce dépôt contient des exercices de réactivation de Python, autour de circuits électriques en série.

## Installation

```
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
```

## Exercices

- `exercices/01_resistances.py` : calcul de la résistance équivalente en série et en parallèle.
- `exercices/02_puissances.py` : calcul de puissances reçues par les résistances.
- `exercices/03_lecture_circuit.py` : calcul de puissances reçues par des résistances extraites d'un fichier txt.
- `exercices/04_circuit_modulaire.py` et `exercices/circuit.py` : même travail que le point précédent, le script affiche les résultats et intercepte les erreurs.
- `exercices/05_numpy.py` : familiarisation avec la bibliothèque numpy.
- `exercices/06_mesures.py` : examen récapitulatif regroupant tout ce qui a été vu dans les exercices précédents

## Exercice 04 : module et script

Le module contient toutes les fonctions dont aura besoin le script, et toutes les erreurs sont interceptées et gérées sans traceback.

Lancement depuis la racine du dépôt :

```
python exercices/04_circuit_modulaire.py
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
    python -m pip install -r requirements.txt
    python exercices/05_numpy.py

> Fonctionnement du script : dossier courant + chemin relatif = endroit réellement cherché.
Donc le script doit être lancé depuis la racine du dépôt pour lire ses données dans data/circuit.txt (un chemin relatif).

### Résultats clés

- **Vectorisation** : méthode vectorisée 31, 34, 42, 54, 57, 63, 81, 91 et 188 fois plus rapide que la boucle for; l'écart peut changer selon l'allocation de ressources du processeur de l'ordinateur selon les sollicitations: temps de déclenchement, priorité accordée à la tâche, engorgement, etc.
- **Surcharge** : Premier dépassement à 10V au lieu du 9.94V théorique, car 10V est la première valeur "dépassante" que la précision de notre array (pas de 0.5V) nous permet de lire.
- **Circuits 2D** : calcul de la résistance série (1120 Ω) et parallèle (50,75 Ω) du premier circuit, et contrôle physique effectué avec R_eq_parallèle < min(résistances du circuit).


## Exercice 06 — Examen de la phase 0 (`06_mesures.py` et `mesures.py`)

**Objectif** : réviser l'ensemble des notions des exercices précédents (lecture de fichier, gestion des erreurs, séparation module/script), en particulier la construction de listes, d'ensembles et de dictionnaires en compréhension.

Le script lit un journal de mesures électriques (capteur, tension, courant), écarte les lignes invalides, calcule les puissances et produit un rapport texte.

### Contenu

| Fonction | Fichier | Rôle |
|---|---|---|
| `lire_mesure` | `mesures.py` | Lit le fichier CSV et renvoie la liste des mesures valides (dictionnaires `capteur`, `tension`, `courant`) ainsi que la liste des motifs de rejet. Les lignes vides et les commentaires (`#`) sont ignorés sans être comptés comme rejets. |
| `puissance` | `mesures.py` | Calcule la puissance P = U × I d'une mesure. |
| `au_dessus_seuil` | `mesures.py` | Sélectionne par compréhension de liste les mesures dont la puissance dépasse strictement le seuil. |
| `mesure_max` | `mesures.py` | Renvoie la mesure de puissance maximale à l'aide de `max(..., key=puissance)`. |
| `moyenne_par_capteur` | `mesures.py` | Regroupe les puissances par capteur (compréhensions d'ensemble et de liste), puis calcule les moyennes par compréhension de dictionnaire. |
| `formater_ligne` | `06_mesures.py` | Met en forme une mesure : `- <capteur> : <U> V x <I> A = <P> W`. |
| `ecrire_rapport` | `06_mesures.py` | Écrit le rapport dans `resultats/rapport.txt`. |
| `main` | `06_mesures.py` | Enchaîne la lecture, les calculs et la rédaction du rapport ; intercepte l'absence du fichier de données. |

### Fichier de test

- `data/mesures.csv` : 9 lignes de mesures et une ligne vide. Deux lignes sont invalides : une valeur non numérique (ligne 6) et une ligne ne comportant que deux champs (ligne 7).

### Lancement

À exécuter depuis la racine du dépôt (le dossier `resultats/` doit exister) :

```
source .venv/Scripts/activate
python exercices/06_mesures.py
```

### Résultats clés

- **Validation** : 7 mesures valides et 2 lignes rejetées, chacune consignée dans le rapport avec son numéro de ligne et le motif du rejet.
- **Mesure maximale** : moteur_A, 228 V × 4,5 A = 1026,0 W.
- **Dépassements** : 4 mesures au-dessus du seuil de 900 W, toutes issues des moteurs A et B.
- **Moyennes par capteur** : moteur_A 981,1 W ; moteur_B 899,0 W ; pompe 300,0 W ; ventilateur 108,0 W.
