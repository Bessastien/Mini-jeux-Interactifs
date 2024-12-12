import random
from base.interface_joueurs import *
from base.sauvegarde import *
from base.outils import *


def titre_choisir_joueur_actif() -> None:
    """
    Cette fonction affiche le titre du choix des joueurs actifs.
    Entrées : aucune
    Sorties : aucune
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Choix des joueurs actifs{reset}")
    print(f"{gris}={reset}" * 85)


def init_fake_joueur(interface: Interface) -> None:
    """
    Cette fonction permet d'initialiser les joueurs.
    Entrées : interface
    Sorties : aucune
    """
    ancienne: int
    ancienne = interface.longueur
    ajouter_joueur(interface, "Joueur 1")
    ajouter_joueur(interface, "Joueur 2")
    ajouter_joueur(interface, "Joueur 3")
    ajouter_joueur(interface, "Joueur 4")
    ajouter_joueur(interface, "Joueur 5")
    ajouter_joueur(interface, "Joueur 6")
    ajouter_joueur(interface, "Joueur 7")
    ajouter_joueur(interface, "Joueur 8")
    ajouter_joueur(interface, "Joueur 9")
    ajouter_joueur(interface, "Joueur 10")

    for i in range(ancienne+1, interface.longueur):
        interface.joueurs[i].score_devinette = random.randint(0, 100)
        interface.joueurs[i].score_allumette = random.randint(0, 100)
        interface.joueurs[i].score_morpion = random.randint(0, 100)
        interface.joueurs[i].score_puissance4 = random.randint(0, 100)

    titre_choisir_joueur_actif()
    print("\n\tJoueurs ajoutés")
    attendre()


def gestion_classement(interface: Interface):
    """
    Cette fonction affiche le classement des pseudos du meilleur au moins bon par jeu dans un tableau.
    Entrées : interface
    Sorties : aucune
    """
    liste_indices_devinette: list[int]
    liste_indices_allumette: list[int]
    liste_indices_morpion: list[int]
    liste_indices_puissance4: list[int]
    i: int
    j: int
    tmp: int

    # Tri des indices des joueurs par scores
    # Tri devinette
    liste_indices_devinette = [i for i in range(interface.longueur)]
    for i in range(len(liste_indices_devinette)):
        for j in range(i + 1, len(liste_indices_devinette)):
            if interface.joueurs[liste_indices_devinette[i]].score_devinette < interface.joueurs[liste_indices_devinette[j]].score_devinette:
                tmp = liste_indices_devinette[i]
                liste_indices_devinette[i] = liste_indices_devinette[j]
                liste_indices_devinette[j] = tmp

    # Tri allumette
    liste_indices_allumette = [i for i in range(interface.longueur)]
    for i in range(len(liste_indices_allumette)):
        for j in range(i + 1, len(liste_indices_allumette)):
            if interface.joueurs[liste_indices_allumette[i]].score_allumette < interface.joueurs[liste_indices_allumette[j]].score_allumette:
                tmp = liste_indices_allumette[i]
                liste_indices_allumette[i] = liste_indices_allumette[j]
                liste_indices_allumette[j] = tmp

    # Tri morpion
    liste_indices_morpion = [i for i in range(interface.longueur)]
    for i in range(len(liste_indices_morpion)):
        for j in range(i + 1, len(liste_indices_morpion)):
            if interface.joueurs[liste_indices_morpion[i]].score_morpion < interface.joueurs[liste_indices_morpion[j]].score_morpion:
                tmp = liste_indices_morpion[i]
                liste_indices_morpion[i] = liste_indices_morpion[j]
                liste_indices_morpion[j] = tmp

    # Tri puissance4
    liste_indices_puissance4 = [i for i in range(interface.longueur)]
    for i in range(len(liste_indices_puissance4)):
        for j in range(i + 1, len(liste_indices_puissance4)):
            if interface.joueurs[liste_indices_puissance4[i]].score_puissance4 < interface.joueurs[liste_indices_puissance4[j]].score_puissance4:
                tmp = liste_indices_puissance4[i]
                liste_indices_puissance4[i] = liste_indices_puissance4[j]
                liste_indices_puissance4[j] = tmp

    # Affichage des scores
    for i in range(interface.longueur):
        print(f"{interface.joueurs[liste_indices_devinette[i]].nom:>15s} : {interface.joueurs[liste_indices_devinette[i]].score_devinette:<8d} "
              f"| {interface.joueurs[liste_indices_allumette[i]].nom:>15s} : {interface.joueurs[liste_indices_allumette[i]].score_allumette:<8d} "
              f"| {interface.joueurs[liste_indices_morpion[i]].nom:>15s} : {interface.joueurs[liste_indices_morpion[i]].score_morpion:<8d} "
              f"| {interface.joueurs[liste_indices_puissance4[i]].nom:>15s} : {interface.joueurs[liste_indices_puissance4[i]].score_puissance4:<8d}")


def classement(interface: Interface):
    """
    Cette fonction affiche le classement des pseudos du meilleur au moins bon par jeu.
    Entrées : interface
    Sorties : aucune
    """
    clear()
    print(f"{gris}={reset}" * 113)
    print(" " * 26 + f"{jaune}Classement des pseudos du meilleur au moins bon par jeu{reset}")
    print(f"{gris}={reset}" * 113)
    print()
    print(f"         {rose}Devinette{reset}         |         {rose}Allumettes{reset}         |           {rose}Morpion{reset}          |        {rose}Puissance 4{reset}")
    gestion_classement(interface)
    print("\n")
    passer()


def affichage_menu_CSS() -> int:
    """
    Cette fonction affiche le menu des scores et sauvegardes.
    Entrées : aucune
    Sorties : choix
    """
    choix: int
    titre_choisir_joueur_actif()
    print(f"\n\t1. Classement des pseudos du {vert}meilleur{reset} au {rouge}moins bon{reset} par jeu")
    print("\t2. Sauvegarder")
    print("\t3. Reset la sauvegarde")
    print("\t4. Importer 10 Joueurs avec scores aléatoires de 0 à 100")
    print("\t5. Retour\n")
    print(f"{gris}={reset}" * 85)
    choix = int(input("Veuillez entrer 1, 2, 3 ou 4 : "))
    return choix


def menu_CSS(interface: Interface):
    """
    Cette fonction permet de choisir une action parmi celles proposées dans le menu des scores et sauvegardes.
    Entrées : aucune
    Sorties : aucune
    """
    choix: int
    choix = 0
    while choix != 5:
        choix = affichage_menu_CSS()
        if choix == 1:
            classement(interface)
        elif choix == 2:
            sauvegarder_interface(interface)
            attendre()
        elif choix == 3:
            reset_interface(interface)
            attendre()
        elif choix == 4:
            init_fake_joueur(interface)
        elif choix == 5:
            clear()
            print(f"{jaune}\n\tRetour au menu principal...{reset}")  # Retour au menu principal (ne se voit pas)
        else:
            print("Choix invalide.")
            attendre()
            menu_CSS(interface)
