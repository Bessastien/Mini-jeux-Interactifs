from base.interface_joueurs import attendre, verifier_si_2_joueurs_actifs, Interface
from base.outils import gris, reset, passer, jaune, rouge
from jeux.puissance4.joueur_puissance4 import jeu_puissance4, titre_puissance4
from jeux.puissance4.bot_puissance4 import bot_vs_bot, joueur_vs_bot

def regles_puissance4() -> None:
    """
    Affiche les règles du jeu de Puissance 4.

    Returns:
        None
    """
    titre_puissance4()
    print("  Le jeu de Puissance 4 se joue sur une grille de 6 lignes et 7 colonnes.")
    print("  Deux joueurs s'affrontent, l'un avec des jetons rouges et l'autre avec des jetons jaunes.")
    print("  Le but du jeu est d'aligner 4 jetons de sa couleur horizontalement, verticalement ou en diagonale.")
    print("  Le premier joueur qui réussit à aligner 4 jetons de sa couleur gagne la partie.")
    print("  Si la grille est pleine et qu'aucun joueur n'a aligné 4 jetons, la partie est nulle.")
    print("  Les joueurs jouent à tour de rôle en choisissant une colonne où placer leur jeton.")
    print("  Le jeton tombe alors dans la colonne choisie et s'arrête lorsqu'il rencontre un autre jeton ou le bas de la grille.")
    print("  Si une colonne est pleine, le joueur doit choisir une autre colonne.")
    print("  Le gagnant remporte un point.")
    print("  Bonne chance !")
    print()
    print(f"{gris}={reset}" * 85)
    passer()

def menu_puissance4() -> int:
    """
    Affiche le menu du jeu Puissance 4 et retourne le choix de l'utilisateur.

    Returns:
        int: Le choix de l'utilisateur.
    """
    choix: int
    titre_puissance4()
    print("\t1. Jouer contre un joueur")
    print("\t2. Jouer contre une machine")
    print("\t3. Faire jouer deux machines l'une contre l'autre")
    print("\t4. Règles")
    print("\t5. Quitter\n")
    print(f"{gris}={reset}" * 85)
    choix = int(input(f"  Veuillez entrer 1, 2, 3, 4 ou 5 \n{jaune} -> {reset} "))
    return choix

def puissance4(interface: Interface) -> None:
    """
    Permet de jouer au jeu de Puissance 4.

    Args:
        interface (Interface): L'interface contenant les joueurs.

    Returns:
        None
    """
    choix: int
    choix = 0
    while choix != 5:
        choix = menu_puissance4()

        if choix == 1:
            if not verifier_si_2_joueurs_actifs(interface):
                print(f"\n\t{rouge}Il n'y a pas deux joueurs actifs.{reset}")
                attendre()
            else:
                jeu_puissance4(interface)
        elif choix == 2:
            joueur_vs_bot(interface)
        elif choix == 3:
            bot_vs_bot()
        elif choix == 4:
            regles_puissance4()
        elif choix == 5:
            print(f"\n\t{jaune}A bientôt !{reset}")
            attendre()
        else:
            print(f"\n\t{rouge}Choix invalide.{reset}")
            attendre()