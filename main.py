from base.interface_joueurs import Interface, recup_joueur1, recup_joueur2
from base.menuJoueurs import menu_joueur
from jeux.menuJeux import menu_jeu
from base.sauvegarde import charger_interface, sauvegarder_interface
from base.menuScoreSave import menu_CSS
from base.outils import clear, attendre, gris, jaune, rouge, reset


def affichage_menu_principal(interface: Interface) -> int:
    """
    Cette fonction affiche le menu principal.
    Entrées : aucune
    Sorties : choix
    """
    choix: int
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Menu Principal{reset}")
    print(f"{gris}={reset}" * 85)
    print(f"\n\tLes joueurs actifs sont : {recup_joueur1(interface)} et {recup_joueur2(interface)}\n")
    print(f"{gris}-{reset}" * 85)
    print("\n\t\t1. Jouer")
    print("\t\t2. Joueurs")
    print("\t\t3. Classement, score et sauvegarde")
    print("\t\t4. Quitter\n")
    print(f"{gris}={reset}" * 85)
    choix = int(input("Veuillez entrer 1, 2, 3 ou 4 : "))
    return choix


def menu_principal():
    """
    Cette fonction permet d'afficher le menu principal.
    Entrées : aucune
    Sorties : aucune
    """
    choix: int
    choix = 0
    interface: Interface
    interface = charger_interface()

    while choix != 4:
        sauvegarder_interface(interface)
        choix = affichage_menu_principal(interface)
        if choix == 1:
            menu_jeu(interface)
        elif choix == 2:
            menu_joueur(interface)
        elif choix == 3:
            menu_CSS(interface)
        elif choix == 4:
            sauvegarder_interface(interface)
            print(f"bisous {rouge}<3{reset}")
        else:
            print(f"{rouge}Choix invalide.{reset}")
            attendre()
            menu_principal()


if __name__ == '__main__':
    menu_principal()
