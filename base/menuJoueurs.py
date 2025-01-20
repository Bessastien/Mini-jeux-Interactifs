from base.interface_joueurs import choisir_joueur_actif, ajouter_joueurs, menu_supprimer_joueur, Interface
from base.outils import clear, gris, jaune, reset, rouge, attendre
from base.sauvegarde import sauvegarder_interface


def afficher_menu_joueur() -> int:
    """
    Cette fonction affiche le menu des joueurs.

    Returns:
        int: Le choix de l'utilisateur parmi les options du menu.
    """
    choix: int
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Menu des Joueurs{reset}")
    print(f"{gris}={reset}" * 85)
    print("\n\t1. Choisir le(s) joueur(s)")
    print("\t2. Créer un(des) joueur(s)")
    print("\t3. Supprimer un joueur")
    print("\t4. Retour\n")
    print(f"{gris}={reset}" * 85)
    choix = int(input("Veuillez entrer 1, 2, 3 ou 4 : "))
    return choix


def menu_joueur(interface: Interface) -> None:
    """
    Cette fonction permet de gérer les actions liées aux joueurs.

    Args:
        interface (Interface): L'interface contenant les joueurs.

    Returns:
        None
    """
    choix: int
    choix = 0
    while choix != 4:
        sauvegarder_interface(interface)
        choix = afficher_menu_joueur()
        if choix == 1:  # Choisir un joueur
            choisir_joueur_actif(interface)
        elif choix == 2:  # Créer un joueur
            ajouter_joueurs(interface)
        elif choix == 3:  # Supprimer un joueur
            menu_supprimer_joueur(interface)
        elif choix == 4:
            clear()
            print(f"{jaune}\n\tRetour au menu principal...{reset}")  # Retour au menu principal (ne se voit pas)
        else:
            print(f"\n\t{rouge}Choix invalide.{reset}")
            attendre()
            menu_joueur(interface)