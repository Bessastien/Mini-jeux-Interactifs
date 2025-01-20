from base.interface_joueurs import afficher_joueurs_scores_actifs, choisir_joueur_actif, verifier_si_1_joueur_actif, Interface
from base.sauvegarde import sauvegarder_interface
from jeux.devinette.jeu_devinette import devinette
from jeux.allumette.jeu_allumette import allumette
from jeux.morpion.jeu_morpion import morpion
from jeux.puissance4.jeu_puissance4 import puissance4
from base.outils import clear, attendre, gris, jaune, rouge, reset


def titre_jeux() -> None:
    """
    Affiche le titre du menu des jeux.

    Returns:
        None
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Menu des Jeux{reset}")
    print(f"{gris}={reset}" * 85)
    print()


def afficher_menu_jeu(interface: Interface) -> int:
    """
    Affiche le menu des jeux et retourne le choix de l'utilisateur.

    Args:
        interface (Interface): L'interface contenant les joueurs.

    Returns:
        int: Le choix de l'utilisateur.
    """
    choix: int
    titre_jeux()
    print("  Le(s) joueur(s) actif(s) sont :")
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
    Permet de choisir un jeu et de le lancer.

    Args:
        interface (Interface): L'interface contenant les joueurs.

    Returns:
        None
    """
    if not verifier_si_1_joueur_actif(interface):
        titre_jeux()
        print(f"\t{rouge}Veuillez d'abord choisir le(s) joueur(s) actif.{reset}")
        choisir_joueur_actif(interface)
        attendre()

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
