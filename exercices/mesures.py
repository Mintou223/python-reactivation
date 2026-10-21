'''Module contenant les fonctions utiles au calcul,
dans le cadre de l'examen de la phase 0 du programme de QML.'''

import math


def lire_mesure(chemin):
    '''Reçoit un fichier;
    Retourne un tuple contenant une liste de dictionnaires
    des valeurs et une liste avec les lignes rejetées'''
    with open(chemin, 'r', encoding="utf-8") as f:
        mesures = []
        rejets = []
        en_tete = f.readline()
        for numero, ligne in enumerate(f, start=2):
            ligne = ligne.strip()
            if ligne.startswith("#") or not ligne:
                continue
            if ligne.count(',') != 2:
                rejets.append(f"ligne {numero} : {len(ligne.split(','))} "
                              f"champs trouvés au lieu de 3")
                continue
            capteur, tension_str, courant_str = [element.strip()
                                                 for element
                                                 in ligne.split(',')]
            try:
                tension = float(tension_str)
                courant = float(courant_str)
            except ValueError as e:
                rejets.append(f"ligne {numero} : {e}")

                continue
            mesures.append({'capteur': capteur,
                            'tension': tension,
                            'courant': courant})
        return (mesures, rejets)


def puissance(m):
    '''Reçoit un dictionnaire;
    Retourne une puissance (float)'''
    p = m['tension'] * m['courant']
    return p


def au_dessus_seuil(mesures, seuil):
    '''Reçoit une liste de dictionnaires;
    Retourne la liste des dictionnaires dont P>seuil'''
    return [m for m in mesures if puissance(m) > seuil]


def mesure_max(mesures):
    """Renvoie le dictionnaire de la mesure de puissance maximale."""
    return max(mesures, key=puissance)


def moyenne_par_capteur(mesures):
    """Reçoit une liste de dictionnaires;
    Retourne un dictionnaire contenant
    la moyenne des puissance par capteur."""
    puissances = {}
    noms = list(dict.fromkeys(m["capteur"] for m in mesures))
    for capteur in noms:
        puissances[capteur] = [puissance(m)
                               for m in mesures if m["capteur"] == capteur]
    return {capteur: sum(p) / len(p) for capteur, p in puissances.items()}
