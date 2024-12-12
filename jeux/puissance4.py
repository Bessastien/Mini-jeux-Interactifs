from base.interface_joueurs import *
from base.outils import *
import random
import time


def titre_puissance4() -> None:
    """
    Cette fonction affiche le titre du jeu de puissance 4.
    Entrées : aucune
    Sorties : aucune
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Puissance 4{reset}")
    print(f"{gris}={reset}" * 85)
    print()


def regles_puissance4() -> None:
    """
    Cette fonction affiche les règles du jeu de puissance 4.
    Entrées : aucune
    Sorties : aucune
    """
    titre_puissance4()
    print("  Le jeu de puissance 4 se joue sur une grille de 6 lignes et 7 colonnes.")
    print("  Deux joueurs s'affrontent, l'un avec des jetons rouges et l'autre avec des jetons jaunes.")
    print("  Le but du jeu est d'aligner 4 jetons de sa couleur horizontalement, verticalement ou en diagonale.")
    print("  Le premier joueur qui réussit à aligner 4 jetons de sa couleur gagne la partie.")
    print("  Si la grille est pleine et qu'aucun joueur n'a aligné 4 jetons, la partie est nulle.")
    print("  Les joueurs jouent à tour de rôle en choisissant une colonne où placer leur jeton.")
    print("  Le jeton tombe alors dans la colonne choisie \n   et s'arrête lorsqu'il rencontre un autre jeton ou le bas de la grille.")
    print("  Si une colonne est pleine, le joueur doit choisir une autre colonne.")
    print("  Le gagnant remporte un point")
    print("  Bonne chance !")
    print()
    print(f"{gris}={reset}" * 85)
    passer()


def afficher_grille(grille: list[list[str]]) -> None:
    """
    Cette fonction affiche la grille du jeu de puissance 4.
    Entrées : grille
    Sorties : aucune
    """
    res: str
    res = ""
    i: int
    res += ("\n\t|01|02|03|04|05|06|07|\n\n")
    for i in range(6):
        res += f"\t"
        for j in range(7):
            res += f"|{grille[i][j]}"
        res += f"|\n"
    res += f"\t======================\n"
    print(res)


def verifier_victoire(grille: list[list[str]]) -> bool:
    """
    Cette fonction permet de vérifier si un joueur a gagné.
    Entrées : grille
    Sorties : booléen
    """
    i: int
    j: int
    # Vérifier les lignes
    for i in range(6):
        for j in range(4):
            if grille[i][j] == grille[i][j + 1] == grille[i][j + 2] == grille[i][j + 3] != '  ':
                return True

    # Vérifier les colonnes
    for i in range(3):
        for j in range(7):
            if grille[i][j] == grille[i + 1][j] == grille[i + 2][j] == grille[i + 3][j] != '  ':
                return True

    # Vérifier les diagonales
    for i in range(3):
        for j in range(4):
            if grille[i][j] == grille[i + 1][j + 1] == grille[i + 2][j + 2] == grille[i + 3][j + 3] != '  ':
                return True
            if grille[i][j + 3] == grille[i + 1][j + 2] == grille[i + 2][j + 1] == grille[i + 3][j] != '  ':
                return True

    return False


def verifier_match_nul(grille: list[list[str]]) -> bool:
    """
    Cette fonction permet de vérifier si la partie est nulle.
    Entrées : grille
    Sorties : booléen
    """
    i: int
    j: int
    for i in range(6):
        for j in range(7):
            if grille[i][j] == '  ':
                return False
    return True


def verifier_colonne_pleine(grille: list[list[str]], colonne: int) -> bool:
    """
    Cette fonction permet de vérifier si une colonne est pleine.
    Entrées : grille, colonne
    Sorties : booléen
    """
    if grille[0][colonne] == '  ':
        return False
    return True


def trouver_ligne_vide(grille: list[list[str]], colonne: int) -> int:
    """
    Cette fonction permet de trouver la première ligne vide dans une colonne.
    Entrées : grille, colonne
    Sorties : ligne
    """
    for i in range(5, -1, -1):
        if grille[i][colonne] == '  ':
            return i
    return -1


def jeu_puissance4(interface: Interface) -> None:
    """
    Cette fonction permet de jouer au jeu de puissance 4.
    Entrées : aucune
    Sorties : aucune
    """
    grille: list[list[str]]
    grille = [['  ' for _ in range(7)] for _ in range(6)]

    joueur_actif: int
    joueur_actif = random.choice([interface.indice_joueur1, interface.indice_joueur2])
    signe_actif: str
    signe_actif = '🔴'

    while not verifier_victoire(grille) and not verifier_match_nul(grille):
        titre_puissance4()
        afficher_grille(grille)
        print(f"\n\tC'est a {get_name(interface, joueur_actif)} {signe_actif} de jouer.\n")
        colonne: int
        colonne = int(input(f"  Veuillez entrer le numéro de la colonne où vous voulez placer votre jeton (1-7) : ")) - 1

        if colonne < 0 or colonne > 6:
            print(f"\n\t{rouge}Colonne invalide.{reset}")
            attendre()
        elif verifier_colonne_pleine(grille, colonne):
            print(f"\n\t{rouge}Colonne pleine.{reset}")
            attendre()
        else:
            ligne: int
            ligne = trouver_ligne_vide(grille, colonne)

            for i in range(ligne + 1):
                grille[i][colonne] = signe_actif
                if i > 0:
                    grille[i-1][colonne] = '  '

                titre_puissance4()
                afficher_grille(grille)
                time.sleep(0.15)

            if verifier_victoire(grille):
                print(f"\n\t{get_name(interface, joueur_actif)} a gagné !")

            if verifier_match_nul(grille):
                print(f"\n\t{jaune}Match nul !{reset}")

            joueur_actif = interface.indice_joueur1 if joueur_actif == interface.indice_joueur2 else interface.indice_joueur2
            signe_actif = '🔴' if signe_actif == '🟡' else '🟡'

    print()
    passer()


def menu_puissance4() -> int:
    """
    Cette fonction affiche le menu du puissance 4.
    Entrées : aucune
    Sorties : choix
    """
    choix: int
    titre_puissance4()
    print("\t1. Jouer")
    print("\t2. Règles")
    print("\t3. Quitter\n")
    print(f"{gris}={reset}" * 85)
    choix = int(input("Veuillez entrer 1, 2 ou 3 : "))
    return choix


def puissance4(interface: Interface) -> None:
    """
    Cette fonction permet de jouer au jeu de puissance 4.
    Entrées : aucune
    Sorties : aucune
    """
    choix: int
    choix = 0
    while choix != 3:
        choix: int
        choix = menu_puissance4()

        if choix == 1:
            jeu_puissance4(interface)
        elif choix == 2:
            regles_puissance4()
        elif choix == 3:
            print(f"\n\t{jaune}A bientôt !{reset}")
            attendre()
        else:
            print(f"\n\t{rouge}Choix invalide.{reset}")
            attendre()
            puissance4(interface)
