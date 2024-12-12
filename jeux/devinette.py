import time
from base.interface_joueurs import *
from base.outils import *


def titre_devinette() -> None:
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Jeu de Devinette{reset}")
    print(f"{gris}={reset}" * 85)
    print("")


def regles_devinette(maximum: int, tentative: int) -> None:
    """
    Cette fonction affiche les règles du jeu de devinette.
    Entrées : aucune
    Sorties : aucune
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


def qui_joue(interface: Interface) -> tuple[int, int]:
    clear()
    choix: int

    titre_devinette()
    choix = int(input(f"Qui choisi le nombre a deviner ? (l'autre devras le trouver, donnez l'indice)\n\t1- {recup_joueur1(interface)}\n\t2- {recup_joueur2(interface)}\n>>> "))

    if choix == 1:
        return interface.indice_joueur1, interface.indice_joueur2
    elif choix == 2:
        return interface.indice_joueur2, interface.indice_joueur1
    else:
        print(f"{rouge}Choix invalide.{reset}")
        attendre()
        return qui_joue(interface)


def jeu_devinette(interface: Interface, maximum: int, tentative: int) -> None:
    """
    Cette fonction permet de jouer au jeu de devinette.
    Entrées : aucune
    Sorties : aucune
    """
    indices: tuple[int, int]
    indices = qui_joue(interface)
    indice_j1: int
    indice_j1 = indices[0]
    indice_j2: int
    indice_j2 = indices[1]
    pseudo_j1: str
    pseudo_j1 = get_name(interface, indice_j1)
    pseudo_j2: str
    pseudo_j2 = get_name(interface, indice_j2)

    #Premiere étape : choix du nombre
    titre_devinette()
    nombre: int
    nombre = int(input(f"\t{pseudo_j1}, veuillez entrer un nombre entre 1 et {maximum} compris : "))
    while nombre < 1 or nombre > maximum:
        clear()
        titre_devinette()
        print(f"{rouge}Nombre invalide.{reset}\n")
        nombre = int(input(f"\t{pseudo_j1}, veuillez entrer un nombre entre 1 et {maximum} compris : "))
    print("\n")
    print(f"{gris}-{reset}" * 85)
    print(f"\nVous avez choisi le nombre {bleu}{nombre}{reset} {magenta}(Message affiché 5s){reset}.\n\n")
    print(f"{gris}={reset}" * 85)
    time.sleep(5)
    clear()


#Deuxieme étape : devinette
    titre_devinette()
    print(f"\t{pseudo_j2}, c'est à vous de jouer !")
    print(f"  Vous avez {tentative} essais pour trouver le nombre compris entre 1 et {maximum} compris.\n")
    print(f"{gris}-{reset}" * 85)
    print()

    essais: int
    essais = 0
    proposition: int
    proposition = 0

    while proposition != nombre and essais != tentative:
        proposition = int(input(f"\n\tVeuillez entrer un nombre : "))
        if proposition == nombre:
            print("ah ?!")
        elif proposition < 1 or proposition > maximum:
            print(f"\n{rouge}Nombre invalide.{reset}")
        elif proposition < nombre:
            print(f"\nLe nombre est plus grand que {proposition}.")
        elif proposition > nombre:
            print(f"\nLe nombre est plus petit que {proposition}.")
        essais += 1
        print(f"Il vous reste {tentative - essais} essais.\n")
        print(f"{gris}-{reset}" * 85)


#Fin du jeu
    print("\n")
    if proposition == nombre:
        print(f"Bravo {pseudo_j2} ! Vous avez trouvé le nombre {nombre} en {essais} essais.")
        ajouter_score_devinette(interface, indice_j2, 1)
    else:
        print(f"Dommage {pseudo_j2} ! le nombre était {nombre}.")
        ajouter_score_devinette(interface, indice_j1, 1)
    print("\n")
    print(f"{gris}={reset}" * 85)
    passer()


def titre_option_devinette() -> None:
    """
    Cette fonction affiche le titre des options du jeu de devinette.
    Entrées : aucune
    Sorties : aucune
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 30 + f"{jaune}Options du jeu de Devinette{reset}")
    print(f"{gris}={reset}" * 85)
    print("")


def menu_option_devinette() -> int:
    """
    Cette fonction affiche les options du jeu de devinette.
    Entrées : aucune
    Sorties : aucune
    """
    titre_option_devinette()
    print("\t1. Changer le nombre de tentatives")
    print("\t2. Changer le maximum de la plage a deviner")
    print("\t3. Retour\n")
    print(f"{gris}={reset}" * 85)
    choix: int
    choix = int(input("Veuillez entrer 1, 2 ou 3 : "))
    return choix


def changer_nombre_tentatives(tentative: int) -> int:
    """
    Cette fonction permet de changer le nombre de tentatives.
    Entrées : aucune
    Sorties : tentative
    """
    titre_option_devinette()
    print(f"\tLe nombre de tentatives actuel est de {tentative}.\n")
    tentative = int(input(f"  Veuillez entrer le nombre de tentative maximum : "))
    print(f"\n\tLe nombre de tentatives a été changé à {tentative}.\n")
    print(f"{gris}={reset}" * 85)
    passer()
    return tentative

def changer_maximum_plage(maximum: int) -> int:
    """
    Cette fonction permet de changer le maximum de la plage a deviner.
    Entrées : aucune
    Sorties : maximum
    """
    titre_option_devinette()
    print(f"\tLe maximum de la plage actuel est de {maximum}.\n")
    maximum = int(input(f"  Veuillez entrer le maximum de la plage a deviner : "))
    print(f"\n\tLe maximum de la plage a été changé à {maximum}.\n")
    print(f"{gris}={reset}" * 85)
    passer()
    return maximum


def option_devinette(maximum: int, tentative: int) -> tuple[int, int]:
    """
    Cette fonction permet de changer les options du jeu de devinette.
    Entrées : aucune
    Sorties : aucune
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
    Cette fonction affiche le menu principal du jeu de devinette.
    Entrées : aucune
    Sorties : choix
    """
    titre_devinette()
    print("\t1. Jouer")
    print("\t2. Règles")
    print("\t3. Option")
    print("\t4. Quitter\n")
    print(f"{gris}={reset}" * 85)
    choix = int(input("Veuillez entrer 1, 2 ou 3 : "))
    return choix


def devinette(interface: Interface) -> None:
    """
    Cette fonction permet de jouer au jeu de devinette.
    Entrées : aucune
    Sorties : aucune
    """
    choix: int
    choix = 0
    maximum: int
    maximum = 500
    tentative: int
    tentative = 10

    while choix != 4:

        choix = afficher_menu_devinette()

        if choix == 1:
            jeu_devinette(interface, maximum, tentative)
        elif choix == 2:
            regles_devinette(maximum, tentative)
        elif choix == 3:
            option : tuple[int, int]
            option = option_devinette(maximum, tentative)
            maximum = option[0]
            tentative = option[1]
        elif choix == 4:
            print(f"\n\t{jaune}A bientôt !{reset}")
            attendre()
        else:
            print(f"\n\t{rouge}Choix invalide.{reset}")
            attendre()
            devinette(interface)
