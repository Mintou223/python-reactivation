"""Script de l'examen de la phase 0 du programme de QML"""
import sys
from mesures import *


SEUIL_W = 900
chemin_lecture = 'data/mesures.csv'
chemin_ecriture = 'resultats/rapport.txt'


def main():
    try:
        mesures, nb_rejetees = lire_mesure(chemin_lecture)
        nb_valides = len(mesures)
        texte = f"Rapport de mesures\n"
        texte += f"Mesures valides : {nb_valides}\n"
        texte += f"Lignes rejetées : {nb_rejetees}\n"
        for m in mesures:
            texte += formater_ligne(m)
        p_max = mesure_max(mesures)
        texte += f"\nMesure maximale : {p_max["capteur"]}"
        texte += f" ({puissance(p_max)} W)\n\n"
        texte += "Mesures au-dessus de 900 W :\n"
        texte += "Mesures au-dessus de 900 W :\n"
        sup_seuil = au_dessus_seuil(mesures, SEUIL_W)
        for m in sup_seuil:
            texte += formater_ligne(m)
        texte += "\nPuissance moyenne par capteur :\n"
        moyennes = moyenne_par_capteur(mesures)
        for cle, valeur in moyennes.items():
            texte += f"- {cle} : {valeur} W\n"
        ecrire_rapport(chemin_ecriture, texte)
        print(f"{nb_valides} mesures valides, {nb_rejetees} lignes "
              f"rejetées — rapport écrit dans resultats/rapport.txt")
    except FileNotFoundError as e:
        print('Fichier introuvable')
        sys.exit(1)


def formater_ligne(m):
    '''Renvoie les données sous format
    "- <capteur> : <U> V x <I> A = <P> W"'''
    capteur, tension, courant = m["capteur"], m["tension"], m["courant"]
    p = puissance(m)
    return f"- {capteur}: {tension}V * {courant}A = {p}W\n"


def ecrire_rapport(chemin, texte):
    '''Ecrit le rapport'''
    with open(str(chemin), 'w', encoding='utf-8') as f:
        f.write(texte)


if __name__ == "__main__":
    main()
