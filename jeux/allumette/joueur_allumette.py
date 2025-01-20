from base.interface_joueurs import get_name, ajouter_score_allumette, Interface
from base.outils import clear, attendre, passer, rouge, bleu, jaune, gris, reset, vert
import random


def titre_allumette() -> None:
    """
    Affiche le titre du jeu d'allumette.

    Returns:
        None
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Jeu de l'allumette{reset}")
    print(f"{gris}={reset}" * 85)
    print()


def tour_joueur_allumette(interface: Interface, nombres_allumettes: int, indice_joueur_actif: int) -> int:
    """
    Cette fonction permet à un joueur de retirer des allumettes.

    Args:
        interface (Interface): L'interface contenant les joueurs.
        nombres_allumettes (int): Le nombre d'allumettes restantes.
        indice_joueur_actif (int): L'indice du joueur actif.

    Returns:
        int: Le nombre d'allumettes restantes.
    """
    allumette_a_retirer: int
    allumette_a_retirer = 0

    if nombres_allumettes == 1:
        allumette_a_retirer = 1
        print(f"\n  {bleu}{get_name(interface, indice_joueur_actif)}{reset}, vous devez retirer la dernière allumette.")
    elif nombres_allumettes == 2:
        while not (allumette_a_retirer == 1 or allumette_a_retirer == 2):
            allumette_a_retirer = int(input(f"\n  {bleu}{get_name(interface, indice_joueur_actif)}{reset}, combien d'allumettes voulez-vous retirer ? (1 ou 2) \n{jaune} -> {reset} "))
            if allumette_a_retirer != 1 and allumette_a_retirer != 2:
                print(f"\n\t{rouge}Choix invalide.{reset}")
    else:
        while not (allumette_a_retirer == 1 or allumette_a_retirer == 2 or allumette_a_retirer == 3):
            allumette_a_retirer = int(input(f"\n  {bleu}{get_name(interface, indice_joueur_actif)}{reset}, combien d'allumettes voulez-vous retirer ? (1, 2 ou 3) \n{jaune} -> {reset} "))
            if allumette_a_retirer != 1 and allumette_a_retirer != 2 and allumette_a_retirer != 3:
                print(f"\n\t{rouge}Choix invalide.{reset}")

    print(f"\n\t{get_name(interface, indice_joueur_actif)} retire {rouge}{allumette_a_retirer}{reset} allumettes.")

    return nombres_allumettes - allumette_a_retirer


def joueur_vs_joueur_allumette(interface: Interface) -> None:
    """
    Permet de jouer au jeu d'allumette entre deux joueurs.

    Args:
        interface (Interface): L'interface contenant les joueurs.

    Returns:
        None
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

        print(f"\tIl reste {rouge}{nombres_allumettes}{reset} allumettes.")

        # un tour de jeu
        nombres_allumettes = tour_joueur_allumette(interface, nombres_allumettes, indice_joueur_actif)

        print()
        print(f"{gris}-{reset}" * 85)
        print()

        # Vérification de la fin de partie
        if nombres_allumettes == 0:
            print(f"  {rouge}{get_name(interface, indice_joueur_actif)}{reset} vous avez perdu !")

            indice_joueur_actif = interface.indice_joueur1 if indice_joueur_actif == interface.indice_joueur2 else interface.indice_joueur2  # Changement de joueur actif
            ajouter_score_allumette(interface, indice_joueur_actif, 1)
            print(f"\n  {vert}{get_name(interface, indice_joueur_actif)}{reset} a gagné la partie !\n")

            print(f"{gris}={reset}" * 85)
            passer()

        indice_joueur_actif = interface.indice_joueur1 if indice_joueur_actif == interface.indice_joueur2 else interface.indice_joueur2  # Changement de joueur actif
