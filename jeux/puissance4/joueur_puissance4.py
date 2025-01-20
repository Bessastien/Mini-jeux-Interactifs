from base.outils import clear, gris, jaune, reset, rouge, attendre, passer
from base.interface_joueurs import get_name, Interface
import random, time

def titre_puissance4() -> None:
    """
    Affiche le titre du jeu Puissance 4.

    Returns:
        None
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Puissance 4{reset}")
    print(f"{gris}={reset}" * 85)
    print()

def afficher_grille(grille: list[list[str]]) -> None:
    """
    Affiche la grille du jeu Puissance 4.

    Args:
        grille (list[list[str]]): La grille de jeu.

    Returns:
        None
    """
    res: str
    res = ""
    i: int
    res += ("\n\t|01|02|03|04|05|06|07|\n\n")
    for i in range(6):
        res += f"\t"
        for j in range(7):
            res += f"|{grille[i][j]}"
        res += f"|\n"
    res += f"\t======================\n"
    print(res)

def verifier_victoire(grille: list[list[str]]) -> bool:
    """
    Vérifie si un joueur a gagné.

    Args:
        grille (list[list[str]]): La grille de jeu.

    Returns:
        bool: True si un joueur a gagné, sinon False.
    """
    i: int
    j: int
    # Vérifier les lignes
    for i in range(6):
        for j in range(4):
            if grille[i][j] == grille[i][j + 1] == grille[i][j + 2] == grille[i][j + 3] != '  ':
                return True

    # Vérifier les colonnes
    for i in range(3):
        for j in range(7):
            if grille[i][j] == grille[i + 1][j] == grille[i + 2][j] == grille[i + 3][j] != '  ':
                return True

    # Vérifier les diagonales
    for i in range(3):
        for j in range(4):
            if grille[i][j] == grille[i + 1][j + 1] == grille[i + 2][j + 2] == grille[i + 3][j + 3] != '  ':
                return True
            if grille[i][j + 3] == grille[i + 1][j + 2] == grille[i + 2][j + 1] == grille[i + 3][j] != '  ':
                return True

    return False

def verifier_match_nul(grille: list[list[str]]) -> bool:
    """
    Vérifie si la partie est nulle.

    Args:
        grille (list[list[str]]): La grille de jeu.

    Returns:
        bool: True si la partie est nulle, sinon False.
    """
    i: int
    j: int
    for i in range(6):
        for j in range(7):
            if grille[i][j] == '  ':
                return False
    return True

def verifier_colonne_pleine(grille: list[list[str]], colonne: int) -> bool:
    """
    Vérifie si une colonne est pleine.

    Args:
        grille (list[list[str]]): La grille de jeu.
        colonne (int): L'indice de la colonne à vérifier.

    Returns:
        bool: True si la colonne est pleine, sinon False.
    """
    if grille[0][colonne] == '  ':
        return False
    return True

def trouver_ligne_vide(grille: list[list[str]], colonne: int) -> int:
    """
    Trouve la première ligne vide dans une colonne.

    Args:
        grille (list[list[str]]): La grille de jeu.
        colonne (int): L'indice de la colonne.

    Returns:
        int: L'indice de la première ligne vide.
    """
    for i in range(5, -1, -1):
        if grille[i][colonne] == '  ':
            return i
    return -1

def coup_joueur(interface: Interface, indice_joueur: int, signe: str, grille: list[list[str]]) -> int:
    """
    Gère le coup d'un joueur.

    Args:
        interface (Interface): L'interface contenant les joueurs.
        indice_joueur (int): L'indice du joueur.
        signe (str): Le signe du joueur.
        grille (list[list[str]]): La grille de jeu.

    Returns:
        int: L'indice de la colonne choisie par le joueur.
    """
    print(f"\n\tC'est a {get_name(interface, indice_joueur)} {signe} de jouer.\n")
    colonne: int
    colonne = int(input(f"  Veuillez entrer le numéro de la colonne où vous voulez placer votre jeton (1-7) \n{jaune} -> {reset} ")) - 1

    if colonne < 0 or colonne > 6:
        print(f"\n\t{rouge}Colonne invalide.{reset}")
        attendre()
        return coup_joueur(interface, indice_joueur, signe, grille)
    elif verifier_colonne_pleine(grille, colonne):
        print(f"\n\t{rouge}Colonne pleine.{reset}")
        attendre()
        return coup_joueur(interface, indice_joueur, signe, grille)

    return colonne

def placer_jeton_animation(grille: list[list[str]], signe: str, colonne: int, ligne: int) -> None:
    """
    Place un jeton dans la grille avec une animation.

    Args:
        grille (list[list[str]]): La grille de jeu.
        signe (str): Le signe du joueur.
        colonne (int): L'indice de la colonne.
        ligne (int): L'indice de la ligne.

    Returns:
        None
    """
    for i in range(ligne + 1):
        grille[i][colonne] = signe
        if i > 0:
            grille[i - 1][colonne] = '  '

        titre_puissance4()
        afficher_grille(grille)
        time.sleep(0.15)

def placer_jeton(grille: list[list[str]], signe: str, colonne: int, ligne: int) -> None:
    """
    Place un jeton dans la grille sans animation.

    Args:
        grille (list[list[str]]): La grille de jeu.
        signe (str): Le signe du joueur.
        colonne (int): L'indice de la colonne.
        ligne (int): L'indice de la ligne.

    Returns:
        None
    """
    grille[ligne][colonne] = signe

def fin_jeu_joueur(interface: Interface, grille: list[list[str]], joueur_actif: int, signe: str) -> None:
    """
    Gère la fin de jeu pour un joueur.

    Args:
        interface (Interface): L'interface contenant les joueurs.
        grille (list[list[str]]): La grille de jeu.
        joueur_actif (int): L'indice du joueur actif.
        signe (str): Le signe du joueur.

    Returns:
        None
    """
    if verifier_victoire(grille):
        print(f"\n\t{get_name(interface, joueur_actif)} ({signe}) a gagné !")

    if verifier_match_nul(grille):
        print(f"\n\t{jaune}Match nul !{reset}")

def jeu_puissance4(interface: Interface) -> None:
    """
    Permet de jouer au jeu Puissance 4.

    Args:
        interface (Interface): L'interface contenant les joueurs.

    Returns:
        None
    """
    grille: list[list[str]]
    grille = [['  ' for _ in range(7)] for _ in range(6)]

    joueur_actif: int
    joueur_actif = random.choice([interface.indice_joueur1, interface.indice_joueur2])
    signe_actif: str
    signe_actif = '🔴'

    while not verifier_victoire(grille) and not verifier_match_nul(grille):
        titre_puissance4()
        afficher_grille(grille)

        colonne: int
        colonne = coup_joueur(interface, joueur_actif, signe_actif, grille)

        ligne: int
        ligne = trouver_ligne_vide(grille, colonne)

        placer_jeton_animation(grille, signe_actif, colonne, ligne)

        fin_jeu_joueur(interface, grille, joueur_actif, signe_actif)

        joueur_actif = interface.indice_joueur1 if joueur_actif == interface.indice_joueur2 else interface.indice_joueur2
        signe_actif = '🔴' if signe_actif == '🟡' else '🟡'

    print()
    passer()