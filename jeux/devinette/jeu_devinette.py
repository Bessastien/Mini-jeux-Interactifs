from base.interface_joueurs import attendre, verifier_si_2_joueurs_actifs,\
    Interface
from base.outils import gris, jaune, reset, rouge, attendre, passer, clear
from jeux.devinette.bot_devinette import boucle_MachineVSMachine, JoueurVSMachine
from jeux.devinette.joueur_devinette import jeu_devinette, titre_devinette


def regles_devinette(maximum: int, tentative: int) -> None:
    """
    Affiche les règles du jeu de devinette.

    Args:
        maximum (int): Le nombre maximum que le joueur peut choisir.
        tentative (int): Le nombre de tentatives autorisées.

    Returns:
        None
    """
    titre_devinette()
    print("  Bienvenue dans le jeu de devinette !")
    print(f"  Le joueur 1 entre un nombre entre 1 et {maximum} compris.")
    print(f"  Le joueur 2 doit deviner ce nombre en moins de {tentative} essais pour gagner la manche.")
    print("  Si le joueur 2 trouve le nombre, il gagne un point.")
    print("  Sinon, le joueur 1 gagne le point.")
    print("  Bonne chance !")
    print("\n")
    print(f"{gris}={reset}" * 85)
    passer()


def titre_option_devinette() -> None:
    """
    Affiche le titre des options du jeu de devinette.

    Returns:
        None
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 30 + f"{jaune}Options du jeu de Devinette{reset}")
    print(f"{gris}={reset}" * 85)
    print("")


def menu_option_devinette() -> int:
    """
    Affiche les options du jeu de devinette et retourne le choix de l'utilisateur.

    Returns:
        int: Le choix de l'utilisateur.
    """
    titre_option_devinette()
    print("\t1. Changer le nombre de tentatives")
    print("\t2. Changer le maximum de la plage a deviner")
    print("\t3. Retour\n")
    print(f"{gris}={reset}" * 85)
    choix: int
    choix = int(input(f"  Veuillez entrer 1, 2 ou 3 \n{jaune} -> {reset} "))
    return choix


def changer_nombre_tentatives(tentative: int) -> int:
    """
    Permet de changer le nombre de tentatives.

    Args:
        tentative (int): Le nombre actuel de tentatives.

    Returns:
        int: Le nouveau nombre de tentatives.
    """
    tentative: int
    titre_option_devinette()
    print(f"\tLe nombre de tentatives actuel est de {tentative}.\n")
    tentative = int(input(f"  Veuillez entrer le nombre de tentative maximum \n{jaune} -> {reset} "))
    print(f"\n\tLe nombre de tentatives a été changé à {tentative}.\n")
    print(f"{gris}={reset}" * 85)
    passer()
    return tentative


def changer_maximum_plage(maximum: int) -> int:
    """
    Permet de changer le maximum de la plage à deviner.

    Args:
        maximum (int): Le maximum actuel de la plage.

    Returns:
        int: Le nouveau maximum de la plage.
    """
    maximum: int
    titre_option_devinette()
    print(f"\tLe maximum de la plage actuel est de {maximum}.\n")
    maximum = int(input(f"  Veuillez entrer le maximum de la plage a deviner \n{jaune} -> {reset} "))
    print(f"\n\tLe maximum de la plage a été changé à {maximum}.\n")
    print(f"{gris}={reset}" * 85)
    passer()
    return maximum


def option_devinette(maximum: int, tentative: int) -> tuple[int, int]:
    """
    Permet de changer les options du jeu de devinette.

    Args:
        maximum (int): Le maximum actuel de la plage.
        tentative (int): Le nombre actuel de tentatives.

    Returns:
        tuple[int, int]: Le nouveau maximum de la plage et le nouveau nombre de tentatives.
    """
    choix: int
    choix = 0
    while choix != 3:
        choix = menu_option_devinette()
        if choix == 1:
            tentative = changer_nombre_tentatives(tentative)
        elif choix == 2:
            maximum = changer_maximum_plage(maximum)
        elif choix == 3:
            print(f"\n\t{jaune}Retour au menu principal...{reset}")
            attendre()
        else:
            print(f"\n\t{rouge}Choix invalide.{reset}")
            attendre()
    return maximum, tentative


def afficher_menu_devinette() -> int:
    """
    Affiche le menu principal du jeu de devinette et retourne le choix de l'utilisateur.

    Returns:
        int: Le choix de l'utilisateur.
    """
    titre_devinette()
    print("\t1. Jouer a deux joueurs")
    print("\t2. Jouer contre une machine")
    print("\t3. Faire jouer deux machines l'une contre l'autre")
    print("\t4. Règles")
    print("\t5. Option")
    print("\t6. Quitter\n")
    print(f"{gris}={reset}" * 85)
    choix = int(input(f"  Veuillez entrer 1, 2, 3, 4, 5 ou 6 \n{jaune} -> {reset} "))
    return choix


def devinette(interface: Interface) -> None:
    """
    Permet de jouer au jeu de devinette.

    Args:
        interface (Interface): L'interface contenant les joueurs.

    Returns:
        None
    """
    choix: int
    choix = 0
    maximum: int
    maximum = 500
    tentative: int
    tentative = 10

    while choix != 6:
        choix = afficher_menu_devinette()

        if choix == 1:
            if not verifier_si_2_joueurs_actifs(interface):
                print(f"\n\t{rouge}Il n'y a pas deux joueurs actifs.{reset}")
                attendre()
            else:
                jeu_devinette(interface, maximum, tentative)
        elif choix == 2:
            JoueurVSMachine(interface, maximum, tentative)
        elif choix == 3:
            boucle_MachineVSMachine(maximum, tentative)
        elif choix == 4:
            regles_devinette(maximum, tentative)
        elif choix == 5:
            option: tuple[int, int]
            option = option_devinette(maximum, tentative)
            maximum = option[0]
            tentative = option[1]
        elif choix == 6:
            print(f"\n\t{jaune}A bientôt !{reset}")
            attendre()
        else:
            print(f"\n\t{rouge}Choix invalide.{reset}")
            attendre()
            devinette(interface)
