"""Script de l'examen de la phase 0 du programme de QML"""
import sys
from pathlib import Path
from mesures import *


SEUIL_W = 900
chemin_lecture = 'data/mesures.csv'
chemin_ecriture = 'resultats/rapport.txt'


def main():
    try:
        mesures, rejets = lire_mesure(chemin_lecture)
        nb_valides = len(mesures)
        nb_rejetees = len(rejets)
        texte = f"Rapport de mesures\n"
        texte += f"Mesures valides : {nb_valides}\n"
        texte += f"Lignes rejetées : {nb_rejetees}\n"
        for i in rejets:
            texte += "- "+i+"\n"
        p_max = mesure_max(mesures)
        texte += f"\nMesure maximale : {p_max["capteur"]}"
        texte += f" ({puissance(p_max)} W)\n\n"
        texte += f"Mesures au-dessus de {SEUIL_W} W :\n"
        sup_seuil = au_dessus_seuil(mesures, SEUIL_W)
        for m in sup_seuil:
            texte += formater_ligne(m)
        texte += "\nPuissance moyenne par capteur :\n"
        moyennes = moyenne_par_capteur(mesures)
        for cle, valeur in moyennes.items():
            texte += f"- {cle} : {valeur:.1f} W\n"
        ecrire_rapport(chemin_ecriture, texte)
        print(f"{nb_valides} mesures valides, {nb_rejetees} lignes "
              f"rejetées — rapport écrit dans resultats/rapport.txt")
    except FileNotFoundError as e:
        print(f'Fichier introuvable ou mauvais chemin: {chemin_lecture}')
        sys.exit(1)


def formater_ligne(m):
    '''Renvoie les données sous format
    "- <capteur> : <U> V x <I> A = <P> W"'''
    capteur, tension, courant = m["capteur"], m["tension"], m["courant"]
    p = puissance(m)
    return f"- {capteur} : {tension} V x {courant} A = {p:.1f} W\n"


def ecrire_rapport(chemin, texte):
    '''Ecrit le rapport, en créant son dossier si nécessaire.'''
    chemin = Path(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(texte)


if __name__ == "__main__":
    main()
