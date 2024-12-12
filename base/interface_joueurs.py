from base.outils import *


class Joueur:
    nom: str
    score_allumette: int
    score_devinette: int
    score_morpion: int
    score_puissance4: int


class Interface:
    joueurs: list[Joueur]
    joueurs = [None] * 30  # On initialise la liste des joueurs à 30.
    longueur: int
    longueur = 0
    indice_joueur1: int
    indice_joueur2: int
    indice_joueur1 = -1  # On initialise les indices des joueurs à -1, car ils ne sont pas encore définis.
    indice_joueur2 = -1


def trouver_joueur(interface: Interface, nom: str) -> int:
    """
    Cette fonction permet de trouver un joueur dans l'interface.
    Entrées : interface, nom
    Sorties : indice du joueur
    """
    i: int
    for i in range(interface.longueur):  # On parcourt la liste des joueurs
        if interface.joueurs[i].nom == nom:  # Si le nom du joueur est égal au nom recherché
            return i  # On retourne l'indice du joueur
    return -1  # Sinon, on retourne -1.


def get_name(interface: Interface, indice_joueur: int) -> str:
    """
    Cette fonction permet de trouver le nom d'un joueur.
    Entrées : interface, indice_joueur
    Sorties : nom
    """
    return interface.joueurs[indice_joueur].nom


def trouver_score_allumette(interface: Interface, indice_joueur: int) -> int:
    """
    Cette fonction permet de trouver le score d'un joueur.
    Entrées : interface, indice_joueur
    Sorties : score
    """
    return interface.joueurs[indice_joueur].score_allumette


def trouver_score_devinette(interface: Interface, indice_joueur: int) -> int:
    """
    Cette fonction permet de trouver le score d'un joueur.
    Entrées : interface, indice_joueur
    Sorties : score
    """
    return interface.joueurs[indice_joueur].score_devinette


def trouver_score_morpion(interface: Interface, indice_joueur: int) -> int:
    """
    Cette fonction permet de trouver le score d'un joueur.
    Entrées : interface, indice_joueur
    Sorties : score
    """
    return interface.joueurs[indice_joueur].score_morpion


def trouver_score_puissance4(interface: Interface, indice_joueur: int) -> int:
    """
    Cette fonction permet de trouver le score d'un joueur.
    Entrées : interface, indice_joueur
    Sorties : score
    """
    return interface.joueurs[indice_joueur].score_puissance4


def recup_joueur1(interface: Interface) -> str:
    """
    Cette fonction permet de récupérer le joueur 1.
    Entrées : interface
    Sorties : joueur 1
    """
    if interface.indice_joueur1 == -1:  # Si le joueur 1 n'est pas défini (indice = -1) on retourne "-"
        return "-"
    return interface.joueurs[interface.indice_joueur1].nom  # Sinon, on retourne le nom du joueur 1.


def recup_joueur2(interface: Interface) -> str:
    """
    Cette fonction permet de récupérer le joueur 2.
    Entrées : interface
    Sorties : joueur 2
    """
    if interface.indice_joueur2 == -1:  # Si le joueur 2 n'est pas défini (indice = -1) on retourne "-"
        return "-"
    return interface.joueurs[interface.indice_joueur2].nom  # Sinon, on retourne le nom du joueur 2.


def ajouter_score_allumette(interface: Interface, indice_joueur: int, score: int) -> None:
    """
    Cette fonction permet d'ajouter un score à un joueur.
    Entrées : interface, indice_joueur, score
    Sorties : aucune
    """
    interface.joueurs[indice_joueur].score_allumette += score


def ajouter_score_devinette(interface: Interface, indice_joueur: int, score: int) -> None:
    """
    Cette fonction permet d'ajouter un score à un joueur.
    Entrées : interface, indice_joueur, score
    Sorties : aucune
    """
    interface.joueurs[indice_joueur].score_devinette += score


def ajouter_score_morpion(interface: Interface, indice_joueur: int, score: int) -> None:
    """
    Cette fonction permet d'ajouter un score à un joueur.
    Entrées : interface, indice_joueur, score
    Sorties : aucune
    """
    interface.joueurs[indice_joueur].score_morpion += score


def ajouter_score_puissance4(interface: Interface, indice_joueur: int, score: int) -> None:
    """
    Cette fonction permet d'ajouter un score à un joueur.
    Entrées : interface, indice_joueur, score
    Sorties : aucune
    """
    interface.joueurs[indice_joueur].score_puissance4 += score


def verifier_joueur(interface: Interface, nom: str) -> bool:
    """
    Cette fonction permet de vérifier si un joueur existe.
    Entrées : interface, nom
    Sorties : booléen
    """
    if trouver_joueur(interface, nom) != -1:  # Joueur trouvé
        return True
    else:
        return False


def verifier_joueur_indice(interface: Interface, indice_joueur: int) -> bool:
    """
    Cette fonction permet de vérifier si un joueur existe.
    Entrées : interface, indice_joueur
    Sorties : booléen
    """
    if 0 <= indice_joueur < interface.longueur:  # Si l'indice est inférieur à la longueur de la liste des joueurs, le joueur existe
        return True
    else:
        return False


def verifier_si_2_joueurs_actifs(interface: Interface) -> bool:
    """
    Cette fonction permet de vérifier si 2 joueurs sont actifs.
    Entrées : interface
    Sorties : booléen
    """
    if interface.indice_joueur1 != -1 and interface.indice_joueur2 != -1:  # Si les indices des joueurs sont définis, on retourne True
        return True
    else:
        return False


def verifier_si_plus2_joueurs(interface: Interface) -> bool:
    """
    Cette fonction permet de vérifier s'il y a au moins 2 joueurs de créer.
    Entrées : interface
    Sorties : booléen
    """
    if interface.longueur >= 2:  # Si la longueur de la liste des joueurs est supérieure ou égale à 2, on retourne True
        return True
    else:
        return False
    

def verifier_si_joueurs_dans_liste(interface: Interface) -> bool:
    """
    Cette fonction permet de vérifier s'il y a des joueurs dans la liste.
    Entrées : interface
    Sorties : booléen
    """
    if interface.longueur > 0:  # Si la longueur de la liste des joueurs est positive, on retourne True
        return True
    else:
        return False


def ajouter_joueur(interface: Interface, nom: str) -> None:
    """
    Cette fonction permet d'ajouter un joueur à l'interface.
    Entrées : interface, nom
    Sorties : aucune
    """
    if verifier_joueur(interface, nom):
        print("\n\tJoueur déjà existant.")

    else:
        # On crée un joueur et on lui attribue un nom, on met ses scores à 0.
        if interface.longueur == 30:
            print(f"\n\t{rouge}Nombre maximum de joueurs atteint.{reset}")
            attendre()
        else:
            joueur = Joueur()
            joueur.nom = nom
            joueur.score_allumette = 0
            joueur.score_devinette = 0
            joueur.score_morpion = 0
            joueur.score_puissance4 = 0
            if interface.longueur == len(interface.joueurs):  # Si la longueur de la liste des joueurs est égale à la longueur de la liste, on ajoute le joueur à la fin.
                interface.joueurs.append(joueur)
            else:
                interface.joueurs[interface.longueur] = joueur
            interface.longueur += 1  # On incrémente la longueur de la liste des joueurs
            print("\n\tJoueur ajouté.")


def ajouter_joueurs(interface: Interface) -> None:
    """
    Cette fonction permet d'ajouter des joueurs à l'interface.
    Entrées : interface
    Sorties : aucune
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Ajout de Joueurs{reset}")
    print(f"{gris}={reset}" * 85)
    print()

    choix: str
    choix = 'o'
    while choix == 'o':
        nom_joueur = input(" Veuillez entrer le nom du joueur a créer (15 caractères max) : ")
        while len(nom_joueur) > 15:
            print(f"\n\t{rouge}Nom trop long.{reset}\n")
            attendre()
            nom_joueur = input(" Veuillez entrer le nom du joueur a créer (15 caractères max) : ")
        ajouter_joueur(interface, nom_joueur)
        choix: str
        print("\n")
        choix = input("Voulez vous ajouter un autre joueur ? (o/n) : ")

        print()
        print(f"{gris}-{reset}" * 85)
        print()


def supprimer_joueur(interface: Interface, indice_joueur: int) -> None:
    """
    Cette fonction permet de supprimer un joueur de l'interface.
    Entrées : interface, nom
    Sorties : aucune
    """
    if verifier_joueur_indice(interface, indice_joueur):  # Si le joueur existe
        if interface.indice_joueur1 == indice_joueur:  # Si le joueur est le joueur 1, on met l'indice du joueur 1 à -1, car il n'existe plus.
            interface.indice_joueur1 = -1
        elif interface.indice_joueur2 == indice_joueur:  # Même chose pour le joueur 2
            interface.indice_joueur2 = -1
        if interface.longueur == 1:  # Si la longueur de la liste des joueurs est de 1, on la vide, car il n'y a plus de joueurs.
            interface.joueurs = []
            interface.longueur = 0
        else:  # Sinon, on met le joueur qui est à la fin de la liste à la place du joueur supprimé
            if interface.indice_joueur1 == interface.longueur:  # Si l'indice du joueur h1 est égal à la longueur de la liste, on le met à l'indice du joueur supprimé, car il a été décalé.
                interface.indice_joueur1 = indice_joueur
            if interface.indice_joueur2 == interface.longueur:  # Même chose pour le joueur 2
                interface.indice_joueur2 = indice_joueur
            interface.joueurs[indice_joueur] = interface.joueurs[interface.longueur - 1]
            interface.longueur -= 1  # On change la longueur de la liste
    else:
        print("Joueur non trouvé.")


def menu_supprimer_joueur(interface: Interface) -> None:
    clear()
    print()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Suppression de Joueurs{reset}")
    print(f"{gris}={reset}" * 85)
    print()

    if not verifier_si_joueurs_dans_liste(interface):
        print("\tVous ne pouvez pas supprimer de joueurs car il n'y en a pas...")
        attendre()
    else:
        afficher_joueurs_scores(interface)
        print(f"{gris}-{reset}" * 85)
        print()
        indice_joueur: int
        indice_joueur = int(input("  Veuillez entrer l'indice du joueur a supprimer : "))
        indice_joueur -= 1
        if not verifier_joueur_indice(interface, indice_joueur):
            print(f"\n\t{rouge}Indice invalide, aucun joueur supprimé.{reset}")
            attendre()
        else:
            sur: str
            sur = input(f"\n\t{rouge}Êtes-vous sûr de vouloir supprimer ce joueur ? (o/n) : {reset}")
            if sur == "o":
                supprimer_joueur(interface, indice_joueur)
                print(f"\nJoueur supprimé.")
                attendre()


def afficher_joueurs_scores(interface: Interface) -> None:
    """
    Cette fonction permet d'afficher les joueurs de l'interface.
    Entrées : interface
    Sorties : aucune
    """
    if interface.longueur == 0:
        print(f"{rouge}\tAucun joueur n'a été ajouté.{reset}")
    else:
        print("       Nom du joueur |  Allumette  |  Devinette  |   Morpion   |   Puissance 4")
        for i in range(interface.longueur):
            print(f"  {i+1}- {interface.joueurs[i].nom:>15s} | {trouver_score_morpion(interface, i):>8d}pts | {trouver_score_allumette(interface, i):>8d}pts | {trouver_score_devinette(interface, i):>8d}pts | {trouver_score_puissance4(interface, i):>8d}pts")
        print("\n")


def afficher_joueurs_scores_actifs(interface: Interface) -> None:
    """
    Cette fonction permet d'afficher les joueurs actifs de l'interface.
    Entrées : interface
    Sorties : aucune
    """
    print("\n                  Allumette     Devinette     Morpion      Puissance 4")
    print(f"{recup_joueur1(interface):>15s} : {interface.joueurs[interface.indice_joueur1].score_allumette:>8d}pts   {interface.joueurs[interface.indice_joueur1].score_devinette:>8d}pts   {interface.joueurs[interface.indice_joueur1].score_morpion:>8d}pts   {interface.joueurs[interface.indice_joueur1].score_puissance4:>8d}pts")
    print(f"{recup_joueur2(interface):>15s} : {interface.joueurs[interface.indice_joueur2].score_allumette:>8d}pts   {interface.joueurs[interface.indice_joueur2].score_devinette:>8d}pts   {interface.joueurs[interface.indice_joueur2].score_morpion:>8d}pts   {interface.joueurs[interface.indice_joueur2].score_puissance4:>8d}pts\n")


def definir_joueur_actif(interface: Interface, indice_joueur: int, numero_joueur: int) -> None:
    """
    Cette fonction permet de définir un joueur actif.
    Entrées : interface, indice_joueur, numero_joueur
    Sorties : aucune
    """
    if numero_joueur == 1:
        interface.indice_joueur1 = indice_joueur
    elif numero_joueur == 2:
        interface.indice_joueur2 = indice_joueur
    else:
        print("Erreur de numero de joueur")


def titre_choisir_joueur_actif() -> None:
    """
    Cette fonction permet d'afficher le titre de la fonction choisir_joueur_actif.
    Entrées : aucune
    Sorties : aucune
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 31 + f"{jaune}Choix des Joueurs Actifs{reset}")
    print(f"{gris}={reset}" * 85)
    print()


def choisir_joueur_actif(interface: Interface) -> None:
    """
    Cette fonction permet de choisir les joueurs actifs.
    Entrées : interface, joueursActifs
    Sorties : aucune
    """

    titre_choisir_joueur_actif()

    if not verifier_si_plus2_joueurs(interface):  # S'il n'y a pas 2 joueurs créés, on demande de les créer
        print(f"\n\tVeuillez créer au {rouge}minimum 2{reset} joueurs avant de pouvoir en choisir.\n")
        passer()

    else:
        afficher_joueurs_scores(interface)
        indice_joueur1: int
        indice_joueur2: int

        print(f"{gris}-{reset}" * 85)
        print()

        # joueur 1
        indice_joueur1 = int(input("  Veuillez entrer l'indice du joueur 1 : "))
        indice_joueur1 -= 1
        if verifier_joueur_indice(interface, indice_joueur1):
            print(f"\n\t{vert}Joueur 1 trouvé{reset}")
        else:
            choix: int
            while not verifier_joueur_indice(interface, indice_joueur1):
                titre_choisir_joueur_actif()
                print(f"{rouge}Joueur 1 non trouvé.{reset}\n")
                print("\t1. Prendre un autre joueur")
                print("\t2. Ajouter un joueur")
                choix = int(input("Veuillez entrer 1 ou 2 : "))
                if choix == 1:
                    titre_choisir_joueur_actif()
                    afficher_joueurs_scores(interface)
                    indice_joueur1 = int(input("  Veuillez entrer l'indice du joueur 1 : "))
                    indice_joueur1 -= 1
                elif choix == 2:
                    titre_choisir_joueur_actif()
                    nom_joueur1: str
                    nom_joueur1 = input("  Veuillez entrer le nom du joueur 1 : ")
                    ajouter_joueur(interface, nom_joueur1)
                    indice_joueur1 = interface.longueur - 1
                else:
                    print(f"\n{rouge}Choix invalide.{reset}")
                    attendre()

        print()
        print(f"{gris}-{reset}" * 85)
        print()

        # joueur 2
        indice_joueur2 = int(input("  Veuillez entrer l'indice du joueur 2 : "))
        indice_joueur2 -= 1
        if verifier_joueur_indice(interface, indice_joueur2):
            print(f"\n\t{vert}Joueur 2 trouvé{reset}")
            print()
            print(f"{gris}={reset}" * 85)
            attendre()
        else:

            choix: int
            while not verifier_joueur_indice(interface, indice_joueur2):
                titre_choisir_joueur_actif()
                print(f"{rouge}Joueur 2 non trouvé.{reset}\n")
                print("\t1. Prendre un autre joueur")
                print("\t2. Ajouter un joueur")
                choix = int(input("Veuillez entrer 1 ou 2 : "))
                if choix == 1:
                    titre_choisir_joueur_actif()
                    afficher_joueurs_scores(interface)
                    indice_joueur2 = int(input("  Veuillez entrer l'indice du joueur 2 : "))
                    indice_joueur2 -= 1
                elif choix == 2:
                    titre_choisir_joueur_actif()
                    nom_joueur2: str
                    nom_joueur2 = input("  Veuillez entrer le nom du joueur 2 : ")
                    ajouter_joueur(interface, nom_joueur2)
                    indice_joueur2 = interface.longueur - 1
                else:
                    print(f"\n{rouge}Choix invalide.{reset}")
                    attendre()

        if indice_joueur1 == indice_joueur2:
            print()
            print(f"{gris}-{reset}" * 85)
            print(f"{rouge}\n\tLes joueurs doivent être différents.{reset}")
            attendre()
            choisir_joueur_actif(interface)

        definir_joueur_actif(interface, indice_joueur1, 1)
        definir_joueur_actif(interface, indice_joueur2, 2)
