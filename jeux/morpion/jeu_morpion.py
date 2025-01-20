from base.interface_joueurs import attendre, verifier_si_2_joueurs_actifs,Interface
from base.outils import gris, reset, jaune, rouge, passer
from jeux.morpion.joueur_morpion import jeu_morpion, titre_morpion
from jeux.morpion.bot_morpion import bot_vs_bot_morpion,\
    joueur_vs_machine_morpion



def regles_morpion() -> None:
    """
    Cette fonction affiche les règles du jeu du morpion.

    Returns:
        None
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



def menu_morpion() -> int:
    """
    Cette fonction affiche le menu du morpion.

    Returns:
        int: Le choix de l'utilisateur.
    """
    choix: int
    titre_morpion()
    print("\t1. Jouer contre un joueur")
    print("\t2. Jouer contre une machine")
    print("\t3. Faire jouer deux machines l'une contre l'autre ")
    print("\t4. Règles")
    print("\t5. Quitter\n")
    print(f"{gris}={reset}" * 85)
    choix = int(input(f"  Veuillez entrer 1, 2 ou 3 \n{jaune} -> {reset} "))
    return choix


def morpion(interface: Interface) -> None:
    """
    Cette fonction permet de jouer au jeu du morpion.

    Args:
        interface (Interface): L'interface des joueurs.

    Returns:
        None
    """
    choix: int
    choix = 0
    while choix != 5:
        choix = menu_morpion()

        if choix == 1:
            if not verifier_si_2_joueurs_actifs(interface):
                print(f"\n\t{rouge}Il n'y a pas deux joueurs actifs.{reset}")
                attendre()
            else:
                jeu_morpion(interface)
        elif choix == 2:
            joueur_vs_machine_morpion(interface)
        elif choix == 3:
            bot_vs_bot_morpion()
        elif choix == 4:
            regles_morpion()
        elif choix == 5:
            print(f"\n\t{jaune}A bientôt !{reset}")
            attendre()
        else:
            print(f"\n\t{rouge}Choix invalide{reset}")
            attendre()
            morpion(interface)
