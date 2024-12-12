from base.interface_joueurs import *
from base.outils import *
import random


def titre_morpion() -> None:
    """
    Cette fonction affiche le titre du jeu du morpion.
    Entrées : aucune
    Sorties : aucune
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Jeu du Morpion{reset}")
    print(f"{gris}={reset}" * 85)
    print()


def regles_morpion() -> None:
    """
    Cette fonction affiche les règles du jeu du morpion.
    Entrées : aucune
    Sorties : aucune
    """
    titre_morpion()
    print("  Bienvenue dans le jeu du morpion !")
    print("  Le jeu se joue à deux joueurs.")
    print("  Les joueurs placent à tour de rôle leur symbole (X ou O) sur une grille de 3x3 cases.")
    print("  Le premier joueur à aligner trois de ses symboles horizontalement, verticalement ou en diagonale gagne la partie.")
    print("  Si toutes les cases sont remplies sans qu'il y ait d'alignement, la partie est déclarée nulle.")
    print("  Le joueur qui commence est choisi aléatoirement.")
    print("  Le gagnant remporte un point.")
    print("  Bonne chance !")
    print("\n")
    print(f"{gris}={reset}" * 85)
    passer()


def affichage_morpion(arrays: list[list[str]]) -> None:
    """
    Cette fonction permet d'afficher le tableau du morpion.
    Entrées : tableau de jeu
    Sorties : aucune
    """
    res: str
    res = f"\n\t{'-' * 19}\n"
    for i in range(3):
        res += f"\t"
        for j in range(3):
            res += f"|  {arrays[i][j]}  "
        res += f"|\n\t{'-' * 19}\n"
    print(res)


def verif_case_vide(arrays: list[list[str]], x: int, y: int) -> bool:
    """
    Cette fonction permet de vérifier si une case est vide.
    Entrées : tableau de jeu, coordonnées de la case
    Sorties : booléen
    """
    if arrays[x][y] == " ":
        return True
    else:
        return False


def verif_victoire(arrays: list[list[str]]) -> tuple[bool, str]:
    """
    Cette fonction permet de vérifier si un joueur a gagné.
    Entrées : tableau de jeu
    Sorties : booléen, signe du joueur gagnant
    """
    i: int
    j: int
    # Vérification des lignes
    for i in range(3):
        if arrays[i][0] == arrays[i][1] == arrays[i][2] != " ":
            return True, arrays[i][0]

    # Vérification des colonnes
    for j in range(3):
        if arrays[0][j] == arrays[1][j] == arrays[2][j] != " ":
            return True, arrays[0][j]

    # Vérification des diagonales
    if arrays[0][0] == arrays[1][1] == arrays[2][2] != " ":
        return True, arrays[0][0]
    if arrays[0][2] == arrays[1][1] == arrays[2][0] != " ":
        return True, arrays[0][2]

    return False, ""


def verif_egalite(arrays: list[list[str]]) -> bool:
    """
    Cette fonction permet de vérifier si la partie est nulle.
    Entrées : tableau de jeu
    Sorties : booléen
    """
    i: int
    j: int
    for i in range(3):
        for j in range(3):
            if arrays[i][j] == " ":
                return False
    return True


def jeu_morpion(interface: Interface) -> None:
    """
    Cette fonction permet de jouer au jeu de devinette.
    Entrées : aucune
    Sorties : aucune
    """

    arrays: list[list[str]]
    arrays = [[" "] * 3 for _ in range(3)]
    joueur_actif_signe: str
    joueur_actif_signe = 'X'
    indice_joueur_actif: int
    indice_joueur_actif = random.choice([interface.indice_joueur1, interface.indice_joueur2])
    couleur_joueur_actif: str
    couleur_joueur_actif = bleu

    while not verif_victoire(arrays)[0] and not verif_egalite(arrays):
        # Changement de joueur
        indice_joueur_actif = interface.indice_joueur1 if indice_joueur_actif == interface.indice_joueur2 else interface.indice_joueur2
        joueur_actif_signe = 'X' if joueur_actif_signe == 'O' else 'O'
        couleur_joueur_actif = bleu if couleur_joueur_actif == rouge else rouge

        titre_morpion()

        print()
        affichage_morpion(arrays)
        print()

        print(f"  {couleur_joueur_actif}{get_name(interface, indice_joueur_actif)} ({joueur_actif_signe}){reset}, c'est à vous de jouer !")
        print("Les lignes et colonnes sont numérotées de 1 à 3.\n")
        x: int
        x = int(input("  - Veuillez entrer la ligne : "))
        while x < 1 or x > 3:
            print(f"\n\t{rouge}Ligne invalide.{reset}\n")
            x = int(input("  - Veuillez entrer la ligne : "))
        y: int
        y = int(input("  - Veuillez entrer la colonne : "))
        while y < 1 or y > 3:
            print(f"\n\t{rouge}Colonne invalide.{reset}\n")
            y = int(input("  - Veuillez entrer la colonne : "))
        if verif_case_vide(arrays, x - 1, y - 1):
            arrays[x - 1][y - 1] = f"{couleur_joueur_actif}{joueur_actif_signe}{reset}"
        else:
            print(f"\n\t{rouge}La case est déjà occupée.{reset}")
            attendre()
            #On change les joueurs comme ça quand la boucle recommence et rechange les joueurs, c'est toujours le bon joueur qui joue.
            indice_joueur_actif = interface.indice_joueur1 if indice_joueur_actif == interface.indice_joueur2 else interface.indice_joueur2
            joueur_actif_signe = 'X' if joueur_actif_signe == 'O' else 'O'
            couleur_joueur_actif = bleu if couleur_joueur_actif == rouge else rouge

    if verif_victoire(arrays)[0]:
        affichage_morpion(arrays)
        print(f"\t{vert}{get_name(interface, indice_joueur_actif)}{reset} a gagné !\n")
        ajouter_score_morpion(interface, indice_joueur_actif, 1)
        passer()

    elif verif_egalite(arrays):
        affichage_morpion(arrays)
        print(f"\t{cyan}Match nul !{reset}\n")
        passer()


def menu_morpion() -> int:
    """
    Cette fonction affiche le menu du morpion.
    Entrées : aucune
    Sorties : choix
    """
    choix: int
    titre_morpion()
    print("\t1. Jouer")
    print("\t2. Règles")
    print("\t3. Quitter\n")
    print(f"{gris}={reset}" * 85)
    choix = int(input("Veuillez entrer 1, 2 ou 3 : "))
    return choix


def morpion(interface: Interface) -> None:
    """
    Cette fonction permet de jouer au jeu du morpion.
    Entrées : aucune
    Sorties : aucune
    """
    choix: int
    choix = 0
    while choix != 3:
        choix = menu_morpion()

        if choix == 1:
            jeu_morpion(interface)
        elif choix == 2:
            regles_morpion()
        elif choix == 3:
            print(f"\n\t{jaune}A bientôt !{reset}")
            attendre()
        else:
            print(f"\n\t{rouge}Choix invalide{reset}")
            attendre()
            morpion(interface)
