from base.interface_joueurs import verifier_si_2_joueurs_actifs, attendre,\
    Interface
from base.outils import gris, reset, passer, attendre, jaune, rouge
from jeux.allumette.joueur_allumette import joueur_vs_joueur_allumette,\
    titre_allumette
from jeux.allumette.bot_allumette import joueur_vs_machine_allumette, machine_vs_machine_allumette


def regles_allumette() -> None:
    """
    Cette fonction affiche les règles du jeu d'allumette.

    Returns:
        None
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


def afficher_menu_allumette() -> int:
    """
    Cette fonction affiche le menu principal du jeu de devinette.

    Returns:
        int: Le choix du joueur.
    """
    choix: int
    titre_allumette()
    print("\t1. Jouer a deux joueurs")
    print("\t2. Jouer contre une machine")
    print("\t3. Faire jouer deux machines l'une contre l'autre ")
    print("\t4. Règles")
    print("\t5. Quitter\n")
    print(f"{gris}={reset}" * 85)
    choix = int(input(f"  Veuillez entrer 1, 2, 3, 4 ou 5 \n{jaune} -> {reset} "))
    return choix


def allumette(interface: Interface) -> None:
    """
    Cette fonction permet de jouer au jeu d'allumette.

    Args:
        interface (Interface): L'interface contenant les joueurs.

    Returns:
        None
    """
    choix: int
    choix = 0
    while choix != 5:

        choix: int
        choix = afficher_menu_allumette()

        if choix == 1:
            if not verifier_si_2_joueurs_actifs(interface):
                print(f"\n\t{rouge}Il n'y a pas deux joueurs actifs.{reset}")
                attendre()
            else:
                joueur_vs_joueur_allumette(interface)
        elif choix == 2:
            joueur_vs_machine_allumette(interface)
        elif choix == 3:
            machine_vs_machine_allumette()
        elif choix == 4:
            regles_allumette()
        elif choix == 5:
            print(f"\n\t{jaune}A bientôt !{reset}")
            attendre()
        else:
            print(f"\n\t{rouge}Choix invalide.{reset}")
            attendre()
            allumette(interface)
