from base.interface_joueurs import *
from base.outils import *
import random


def titre_allumette() -> None:
    """
    Cette fonction affiche le titre du jeu d'allumette.
    Entrées : aucune
    Sorties : aucune
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Jeu de l'allumette{reset}")
    print(f"{gris}={reset}" * 85)
    print()


def regles_allumette() -> None:
    """
    Cette fonction affiche les règles du jeu d'allumette.
    Entrées : aucune
    Sorties : aucune
    """
    titre_allumette()
    print("  Bienvenue dans le jeu d'allumette !")
    print("  Le jeu se joue à deux joueurs.")
    print("  Il y a 20 allumettes au départ.")
    print("  Chaque joueur peut retirer 1, 2 ou 3 allumettes")
    print("  Le joueur qui retire la dernière allumette a perdu.")
    print("  Le gagnant remporte un point.")
    print("  Bonne chance !")
    print()
    print(f"{gris}={reset}" * 85)
    passer()


def jeu_allumette(interface: Interface) -> None:
    """
    Cette fonction permet de jouer au jeu d'allumette.
    Entrées : aucune
    Sorties : aucune
    """
    nombres_allumettes: int
    nombres_allumettes = 20
    indice_joueur_actif: int
    indice_joueur_actif = random.choice([interface.indice_joueur1, interface.indice_joueur2])

    titre_allumette()
    print(f"\t{bleu}{get_name(interface, indice_joueur_actif)}{reset} commence la partie !\n")
    print(f"{gris}-{reset}" * 85)
    attendre()

    while nombres_allumettes > 0:

        titre_allumette()

        allumette_a_retirer: int
        allumette_a_retirer = 0  # Reinitialisation du nombre d'allumettes à retirer
        indice_joueur_actif = interface.indice_joueur1 if indice_joueur_actif == interface.indice_joueur2 else interface.indice_joueur2  # Changement de joueur actif

        print(f"\n\tIl reste {rouge}{nombres_allumettes}{reset} allumettes.")

        #Vérification du nombre d'allumettes à retirer
        if nombres_allumettes == 1:
            allumette_a_retirer = 1
            print(f"\n  {bleu}{get_name(interface, indice_joueur_actif)}{reset}, vous devez retirer la dernière allumette.")
        elif nombres_allumettes == 2:
            while not (allumette_a_retirer == 1 or allumette_a_retirer == 2):
                allumette_a_retirer = int(input(f"\n  {bleu}{get_name(interface, indice_joueur_actif)}{reset}, combien d'allumettes voulez-vous retirer ? (1 ou 2) : "))
                if allumette_a_retirer != 1 and allumette_a_retirer != 2:
                    print(f"\n\t{rouge}Choix invalide.{reset}")
        else:
            while not (allumette_a_retirer == 1 or allumette_a_retirer == 2 or allumette_a_retirer == 3):
                allumette_a_retirer = int(input(f"\n  {bleu}{get_name(interface, indice_joueur_actif)}{reset}, combien d'allumettes voulez-vous retirer ? (1, 2 ou 3) : "))
                if allumette_a_retirer != 1 and allumette_a_retirer != 2 and allumette_a_retirer != 3:
                    print(f"\n\t{rouge}Choix invalide.{reset}")

        print(f"\n\t{get_name(interface, indice_joueur_actif)} retire {rouge}{allumette_a_retirer}{reset} allumettes.")

        print()
        print(f"{gris}-{reset}" * 85)
        print()

        #Retrait des allumettes
        nombres_allumettes -= allumette_a_retirer

        #Vérification de la fin de partie
        if nombres_allumettes == 0:
            print(f"  {rouge}{get_name(interface, indice_joueur_actif)}{reset} vous avez perdu !")

            indice_joueur_actif = interface.indice_joueur1 if indice_joueur_actif == interface.indice_joueur2 else interface.indice_joueur2  # Changement de joueur actif
            ajouter_score_allumette(interface, indice_joueur_actif, 1)
            print(f"\n  {vert}{get_name(interface, indice_joueur_actif)}{reset} a gagné la partie !\n")

            print(f"{gris}={reset}" * 85)
            passer()


def afficher_menu_allumette() -> int:
    """
    Cette fonction affiche le menu principal du jeu de devinette.
    Entrées : aucune
    Sorties : choix
    """
    choix: int
    titre_allumette()
    print("\t1. Jouer")
    print("\t2. Règles")
    print("\t3. Quitter\n")
    print(f"{gris}={reset}" * 85)
    choix = int(input("Veuillez entrer 1, 2 ou 3 : "))
    return choix


def allumette(interface: Interface) -> None:
    """
    Cette fonction permet de jouer au jeu d'allumette.
    Entrées : aucune
    Sorties : aucune
    """
    choix: int
    choix = 0
    while choix != 3:

        choix: int
        choix = afficher_menu_allumette()

        if choix == 1:
            jeu_allumette(interface)
        elif choix == 2:
            regles_allumette()
        elif choix == 3:
            print(f"\n\t{jaune}A bientôt !{reset}")
            attendre()
        else:
            print(f"\n\t{rouge}Choix invalide.{reset}")
            attendre()
            allumette(interface)
