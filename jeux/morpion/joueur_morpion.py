from base.interface_joueurs import Interface, get_name, ajouter_score_morpion
from base.outils import clear, reset, jaune, gris, rouge, bleu, vert, cyan, passer, attendre
import random


def titre_morpion() -> None:
    """
    Cette fonction affiche le titre du jeu du morpion.

    Returns:
        None
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Jeu du Morpion{reset}")
    print(f"{gris}={reset}" * 85)
    print()


def affichage_morpion(grille: list[list[str]]) -> None:
    """
    Cette fonction permet d'afficher le tableau du morpion.

    Args:
        grille (list[list[str]]): Le tableau de jeu.

    Returns:
        None
    """
    res: str
    res = f"\n\t{'-' * 19}\n"
    for i in range(3):
        res += f"\t"
        for j in range(3):
            res += f"|  {grille[i][j]}  "
        res += f"|\n\t{'-' * 19}\n"
    print(res)


def verif_case_vide(grille: list[list[str]], x: int, y: int) -> bool:
    """
    Cette fonction permet de vérifier si une case est vide.

    Args:
        grille (list[list[str]]): Le tableau de jeu.
        x (int): La ligne de la case.
        y (int): La colonne de la case.

    Returns:
        bool: True si la case est vide, False sinon.
    """
    if grille[x][y] == " ":
        return True
    else:
        return False


def verif_victoire(grille: list[list[str]]) -> tuple[bool, str]:
    """
    Cette fonction permet de vérifier si un joueur a gagné.

    Args:
        grille (list[list[str]]): Le tableau de jeu.

    Returns:
        tuple[bool, str]: Un tuple contenant un booléen indiquant si un joueur a gagné et le signe du joueur gagnant.
    """
    i: int
    j: int
    # Vérification des lignes
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != " ":
            return True, grille[i][0]

    # Vérification des colonnes
    for j in range(3):
        if grille[0][j] == grille[1][j] == grille[2][j] != " ":
            return True, grille[0][j]

    # Vérification des diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] != " ":
        return True, grille[0][0]
    if grille[0][2] == grille[1][1] == grille[2][0] != " ":
        return True, grille[0][2]

    return False, ""


def verif_egalite(grille: list[list[str]]) -> bool:
    """
    Cette fonction permet de vérifier si la partie est nulle.

    Args:
        grille (list[list[str]]): Le tableau de jeu.

    Returns:
        bool: True si la partie est nulle, False sinon.
    """
    i: int
    j: int
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                return False
    return True


def coup_joueur_morpion(grille: list[list[str]], couleur: str, interface: Interface, indice_joueur: int, signe: str) -> list[list[str]]:
    """
    Cette fonction permet à un joueur de jouer un coup.

    Args:
        grille (list[list[str]]): grille de jeu
        couleur (str): couleur du joueur
        interface (Interface): interface des joueurs
        indice_joueur (int): indice du joueur
        signe (str): signe du joueur

    Returns:
        list[list[str]]: grille de jeu

    """
    print(f"  {couleur}{get_name(interface, indice_joueur)} ({signe}){reset}, c'est à vous de jouer !")
    print("Les lignes et colonnes sont numérotées de 1 à 3.\n")
    x: int
    x = int(input(f"  - Veuillez entrer la ligne \n{jaune} -> {reset} "))
    while x < 1 or x > 3:
        print(f"\n\t{rouge}Ligne invalide.{reset}\n")
        x = int(input(f"  - Veuillez entrer la ligne \n{jaune} -> {reset} "))
    y: int
    y = int(input(f"  - Veuillez entrer la colonne \n{jaune} -> {reset} "))
    while y < 1 or y > 3:
        print(f"\n\t{rouge}Colonne invalide.{reset}\n")
        y = int(input(f"  - Veuillez entrer la colonne \n{jaune} -> {reset} "))
    if verif_case_vide(grille, x - 1, y - 1):
        grille[x - 1][y - 1] = f"{couleur}{signe}{reset}"
    else:
        print(f"\n\t{rouge}La case est déjà occupée.{reset}")
        attendre()
        # On change les joueurs comme ça quand la boucle recommence et rechange les joueurs, c'est toujours le bon joueur qui joue.
        indice_joueur_actif = interface.indice_joueur1 if indice_joueur == interface.indice_joueur2 else interface.indice_joueur2
        joueur_actif_signe = 'X' if signe == 'O' else 'O'
        couleur_joueur_actif = bleu if couleur == rouge else rouge

    return grille


def fin_jeu_joueur_morpion(interface: Interface, grille: list[list[str]], indice_joueur: int) -> None:
    """
    Cette fonction permet de vérifier si un joueur a gagné ou si la partie est nulle.

    Args:
        interface (Interface): interface des joueurs
        grille (list[list[str]]): grille de jeu
        indice_joueur (int): indice du joueur

    Returns:
        None

    """
    if verif_victoire(grille)[0]:
        affichage_morpion(grille)
        print(f"\t{vert}{get_name(interface, indice_joueur)}{reset} a gagné !\n")
        ajouter_score_morpion(interface, indice_joueur, 1)
        passer()

    elif verif_egalite(grille):
        affichage_morpion(grille)
        print(f"\t{cyan}Match nul !{reset}\n")
        passer()


def jeu_morpion(interface: Interface) -> None:
    """
    Cette fonction permet de jouer au jeu de devinette.

    Args:
        interface (Interface): L'interface des joueurs.

    Returns:
        None
    """
    grille: list[list[str]]
    grille = [[" "] * 3 for _ in range(3)]
    joueur_actif_signe: str
    joueur_actif_signe = 'X'
    indice_joueur_actif: int
    indice_joueur_actif = random.choice([interface.indice_joueur1, interface.indice_joueur2])
    couleur_joueur_actif: str
    couleur_joueur_actif = bleu

    while not verif_victoire(grille)[0] and not verif_egalite(grille):
        # Changement de joueur
        indice_joueur_actif = interface.indice_joueur1 if indice_joueur_actif == interface.indice_joueur2 else interface.indice_joueur2
        joueur_actif_signe = 'X' if joueur_actif_signe == 'O' else 'O'
        couleur_joueur_actif = bleu if couleur_joueur_actif == rouge else rouge

        titre_morpion()

        print()
        affichage_morpion(grille)
        print()

        grille = coup_joueur_morpion(grille, couleur_joueur_actif, interface, indice_joueur_actif, joueur_actif_signe)

    fin_jeu_joueur_morpion(interface, grille, indice_joueur_actif)
