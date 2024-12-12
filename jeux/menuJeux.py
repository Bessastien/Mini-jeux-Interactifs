from base.interface_joueurs import *
from base.sauvegarde import sauvegarder_interface
from jeux.devinette import devinette
from jeux.allumette import allumette
from jeux.morpion import morpion
from jeux.puissance4 import puissance4
from base.outils import *


def titre_jeux() -> None:
    """
    Cette fonction affiche le titre du menu des jeux.
    Entrées : aucune
    Sorties : aucune
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Menu des Jeux{reset}")
    print(f"{gris}={reset}" * 85)
    print()


def afficher_menu_jeu(interface: Interface) -> int:
    """
    Cette fonction affiche le menu des jeux.
    Entrées : aucune
    Sorties : choix
    """
    choix: int
    titre_jeux()
    print("  Les joueurs actifs sont :")
    afficher_joueurs_scores_actifs(interface)
    print(f"{gris}-{reset}" * 85)
    print("\n\t\t1. Devinette")
    print("\t\t2. Allumette")
    print("\t\t3. Morpion")
    print("\t\t4. Puissance 4")
    print("\t\t5. Retour\n")
    print(f"{gris}={reset}" * 85)
    choix = int(input("Veuillez entrer 1, 2, 3, 4 ou 5 : "))
    return choix


def menu_jeu(interface: Interface) -> None:
    """
    Cette fonction permet de choisir un jeu.
    Entrées : aucune
    Sorties : aucune
    """
    if not verifier_si_2_joueurs_actifs(interface):
        titre_jeux()
        print(f"\t{rouge}Veuillez d'abord choisir les joueurs actif.{reset}")
        attendre()
    else:
        choix: int
        choix = 0
        while choix != 5:
            sauvegarder_interface(interface)
            choix = afficher_menu_jeu(interface)
            if choix == 1:  # Lance jeu devinette
                devinette(interface)
            elif choix == 2:
                allumette(interface)
            elif choix == 3:
                morpion(interface)
            elif choix == 4:
                puissance4(interface)
            elif choix == 5:
                clear()
                print(f"{jaune}\n\tRetour au menu principal...{reset}")  # Retour au menu principal (ne se voit pas)
            else:
                print(f"{rouge}Choix invalide.{reset}")
                attendre()
                menu_jeu(interface)
