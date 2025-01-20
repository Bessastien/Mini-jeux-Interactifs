from base.outils import vert, cyan, rouge, bleu, gris, jaune, orange, passer, reset
from base.interface_joueurs import Interface
from jeux.morpion.joueur_morpion import fin_jeu_joueur_morpion, verif_victoire,affichage_morpion, verif_egalite, titre_morpion, coup_joueur_morpion
import random, time


def verif_victoire_cible(grille: list[list[str]], symbole: str) -> bool:
    """
    Vérifie si un joueur a gagné en alignant trois symboles identiques.

    Args:
        grille (list[list[str]]): La grille de jeu du morpion.
        symbole (str): Le symbole du joueur à vérifier.

    Returns:
        bool: True si le joueur a gagné, sinon False.
    """
    # Vérification des lignes
    i: int
    j: int
    victoire_ligne: bool
    victoire_diag1: bool
    victoire_diag2: bool

    for i in range(3):
        victoire_ligne = True
        for j in range(3):
            if grille[i][j] != symbole:
                victoire_ligne = False
        if victoire_ligne:
            return True

    # Vérification des colonnes
    for j in range(3):
        victoire_colonne = True
        for i in range(3):
            if grille[i][j] != symbole:
                victoire_colonne = False
        if victoire_colonne:
            return True

    # Vérification première diagonale (haut-gauche à bas-droite)
    victoire_diag1 = True
    for i in range(3):
        if grille[i][i] != symbole:
            victoire_diag1 = False
    if victoire_diag1:
        return True

    # Vérification deuxième diagonale (haut-droite à bas-gauche)
    victoire_diag2 = True
    for i in range(3):
        if grille[i][2 - i] != symbole:
            victoire_diag2 = False
    if victoire_diag2:
        return True

    # Si aucune condition de victoire n'est remplie
    return False


def coups_possibles(grille: list[list[str]]) -> list[tuple[int, int]]:
    """
    Renvoie une liste des coordonnées des cases vides dans la grille.

    Args:
        grille (list[list[str]]): La grille de jeu du morpion.

    Returns:
        list[tuple[int, int]]: Liste des coordonnées des cases vides.
    """
    i: int
    j: int
    return [(i, j) for i in range(3) for j in range(3) if grille[i][j] == " "]


def coup_morpion_n1(grille: list[list[str]], symbole_bot: str) -> list[list[str]]:
    """
    Bot niveau 1 : Effectue un coup aléatoire.

    Args:
        grille (list[list[str]]): La grille de jeu du morpion.
        symbole_bot (str): Le symbole du bot.

    Returns:
        list[list[str]]: La grille mise à jour après le coup du bot.
    """
    cases_vides: list[tuple[int, int]]
    i: int
    j: int
    # Récupérer toutes les cases vides.
    cases_vides = coups_possibles(grille)
    if cases_vides:
        # Choisir une case vide aléatoire.
        i, j = random.choice(cases_vides)
        grille[i][j] = symbole_bot
    return grille


def coup_morpion_n3(grille: list[list[str]], symbole_bot: str, symbole_adversaire: str) -> list[list[str]]:
    """
    Bot niveau 3 : Opportuniste (attaque et défense simple).

    Args:
        grille (list[list[str]]): La grille de jeu du morpion.
        symbole_bot (str): Le symbole du bot.
        symbole_adversaire (str): Le symbole de l'adversaire.

    Returns:
        list[list[str]]: La grille mise à jour après le coup du bot.
    """
    i: int
    j: int
    # Vérifier si le bot peut gagner au prochain coup.
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = symbole_bot
                if verif_victoire_cible(grille, symbole_bot):
                    return grille
                grille[i][j] = " "  # Annuler le coup si pas gagnant.

    # Bloquer un coup gagnant de l'adversaire.
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = symbole_adversaire
                if verif_victoire_cible(grille, symbole_adversaire):
                    grille[i][j] = symbole_bot
                    return grille
                grille[i][j] = " "  # Annuler le coup si pas menaçant.

    # Sinon, jouer comme le bot niveau 1 (coup aléatoire).
    return coup_morpion_n1(grille, symbole_bot)


def coup_morpion_n2(grille: list[list[str]], symbole_bot: str, symbole_adversaire: str) -> list[list[str]]:
    """
    Bot ayant 50% de chance de jouer aleatoirement et 50% de chance d'avoir un strategie.

    Args:
        grille (list[list[int]]) : le grille de jeu du morpion
        symbole_bot (str): le symbole du bot
        symbole_adversaire (str): le symbole de l'adversaire

    Returns:
        list[list[int]]: la grille mise à jour après le coup

    """
    if random.choice([True, False]):
        return coup_morpion_n1(grille, symbole_bot)
    return coup_morpion_n3(grille, symbole_bot, symbole_adversaire)


def coup_machine(grille: list[list[str]], niveau: int, bot: str = 'O', adversaire: str = 'X') -> list[list[str]]:
    """
    Effectue un coup de la machine en fonction du niveau spécifié.

    Args:
        grille (list[list[str]]): La grille de jeu du morpion.
        niveau (int): Le niveau de la machine (1, 2 ou 3).
        bot (str, optional): Le symbole du bot. Par défaut 'O'.
        adversaire (str, optional): Le symbole de l'adversaire. Par défaut 'X'.

    Returns:
        list[list[str]]: La grille mise à jour après le coup du bot.
    """
    if niveau == 1:
        grille = coup_morpion_n1(grille, bot)
    elif niveau == 2:
        grille = coup_morpion_n2(grille, bot, adversaire)
    else:
        grille = coup_morpion_n3(grille, bot, adversaire)
    return grille


def fin_jeu_bot_morpion(grille: list[list[str]], niveau: int) -> bool:
    """
    Vérifie la fin du jeu pour le bot et affiche le résultat.

    Args:
        grille (list[list[str]]): La grille de jeu du morpion.
        niveau (int): Le niveau du bot.

    Returns:
        bool: True si le bot a gagné, False en cas de match nul ou si le jeu continue.
    """
    if verif_victoire(grille)[0]:
        affichage_morpion(grille)
        print(f"\t{vert}Le bot de niveau {niveau}{reset} a gagné !\n")
        return True

    elif verif_egalite(grille):
        affichage_morpion(grille)
        print(f"\t{cyan}Match nul !{reset}\n")
        return False

    return False


def gestion_joueur_machine_morpion(interface: Interface, niveau: int) -> None:
    """
    Gère une partie de morpion entre un joueur et une machine.

    Args:
        interface (Interface): L'interface contenant les joueurs.
        niveau (int): Le niveau de la machine (1, 2 ou 3).

    Returns:
        None
    """
    grille: list[list[str]]
    grille = [[" "] * 3 for _ in range(3)]
    joueur_actif_signe: str
    joueur_actif_signe = 'X'
    indice_joueur_actif: int
    indice_joueur_actif = random.choice([interface.indice_joueur1, -1])
    couleur_joueur_actif: str
    couleur_joueur_actif = bleu

    titre_morpion()
    if indice_joueur_actif == -1:
        print("  Le joueur commence")
    elif indice_joueur_actif == interface.indice_joueur1:
        print("  La machine commence")

    while not verif_victoire(grille)[0] and not verif_egalite(grille):
        # Changement de joueur
        indice_joueur_actif = interface.indice_joueur1 if indice_joueur_actif == -1 else -1
        joueur_actif_signe = 'X' if joueur_actif_signe == 'O' else 'O'
        couleur_joueur_actif = bleu if couleur_joueur_actif == rouge else rouge

        print()
        print(f"{gris}-{reset}" * 85)
        print()

        print()
        affichage_morpion(grille)
        print()

        if indice_joueur_actif == interface.indice_joueur1:
            grille = coup_joueur_morpion(grille, couleur_joueur_actif, interface, indice_joueur_actif, joueur_actif_signe)
        else:
            grille = coup_machine(grille, niveau)

    print()
    print(f"{gris}={reset}" * 85)
    print()

    if indice_joueur_actif == interface.indice_joueur1:
        fin_jeu_joueur_morpion(interface, grille, indice_joueur_actif)
    else:
        fin_jeu_bot_morpion(grille, niveau)
        passer()


def joueur_vs_machine_morpion(interface: Interface) -> None:
    """
    Gère une partie de morpion entre un joueur et une machine.

    Args:
        interface (Interface): L'interface contenant les joueurs.

    Returns:
        None
    """
    titre_morpion()

    print("  Veuillez choisir le niveau de la machine :")
    print("\t1. Niveau 1")
    print("\t2. Niveau 2")
    print("\t3. Niveau 3")
    niveau_machine: int
    niveau_machine = int(input(f"  Votre choix \n{jaune} -> {reset}"))
    while niveau_machine != 1 and niveau_machine != 2 and niveau_machine != 3:
        print(f"{rouge}Niveau de la machine invalide.{reset}")
        niveau_machine = int(input(f"  Votre choix \n{jaune} -> {reset}"))
    gestion_joueur_machine_morpion(interface, niveau_machine)


def gestion_machine_vs_machine_morpion(niveau_machine1: int, niveau_machine2: int) -> int:
    """
    Gère une partie de morpion entre deux machines.

    Args:
        niveau_machine1 (int): Le niveau de la première machine.
        niveau_machine2 (int): Le niveau de la deuxième machine.

    Returns:
        int: L'indice de la machine gagnante (1 ou 2).
    """
    grille: list[list[str]]
    grille = [[" "] * 3 for _ in range(3)]
    niveau: tuple[int, int]
    niveau = (niveau_machine1, niveau_machine2)
    clq: int
    clq = random.choice([1, 2])
    signe: str
    signe = 'X' if clq == 1 else 'O'

    print(f"  La machine de niveau {niveau[clq-1]} commence avec \"{signe}\" comme signe (machine n°{clq})")
    print()
    print(f"{gris}-{reset}" * 85)
    print()

    while not verif_victoire(grille)[0] and not verif_egalite(grille):
        grille = coup_machine(grille, niveau[clq - 1], 'X' if clq == 1 else 'O', 'X' if clq == 2 else 'O')
        print(f"  Au tour de la machine de niveau {niveau[clq-1]} (n°{clq})")
        affichage_morpion(grille)
        print()
        print(f"{gris}-{reset}" * 85)
        print()
        clq = 1 if clq == 2 else 2
        signe = 'X' if clq == 1 else 'O'

    clq = 1 if clq == 2 else 2
    if fin_jeu_bot_morpion(grille, niveau[clq - 1]):
        return clq
    return 0


def boucle_machine_vs_machine_morpion(niveau_machine1: int, niveau_machine2: int, tours: int):
    """
    Gère une série de parties de morpion entre deux machines et affiche les scores.

    Args:
        niveau_machine1 (int): Le niveau de la première machine.
        niveau_machine2 (int): Le niveau de la deuxième machine.
        tours (int): Le nombre de tours à jouer.

    Returns:
        None
    """
    score_machine1: int
    score_machine1 = 0
    score_machine2: int
    score_machine2 = 0
    nul: int
    nul = 0
    res: int

    start: float
    start = time.time()

    titre_morpion()
    for _ in range(tours):
        res = gestion_machine_vs_machine_morpion(niveau_machine1, niveau_machine2)
        if res == 1:
            score_machine1 += 1
        elif res == 2:
            score_machine2 += 1
        else:
            nul += 1

        print()
        print(f"{gris}={reset}" * 85)
        print()

    print(f"{orange}Fin de la partie !{reset}")
    print()

    temps: float
    temps = time.time() - start
    temps = round(temps, 2)

    print(f"Score de la machine 1 (niveau : {niveau_machine1}) : {score_machine1}")
    print(f"Score de la machine 2 (niveau : {niveau_machine2}) : {score_machine2}")
    print(f"Match nul(s) : {nul}")
    print(f"Temps d'exécution du programme : {temps}")
    print()
    passer()


def bot_vs_bot_morpion() -> None:
    """
    Démarre une partie de morpion entre deux machines en demandant les niveaux et le nombre de tours.

    Returns:
        None
    """
    titre_morpion()

    print("  Veuillez choisir le niveau de la machine 1 :")
    print("\t1. Niveau 1")
    print("\t2. Niveau 2")
    print("\t3. Niveau 3")
    niveau_machine1: int
    niveau_machine1 = int(input(f"  Votre choix \n{jaune} -> {reset}"))
    while niveau_machine1 != 1 and niveau_machine1 != 2 and niveau_machine1 != 3:
        print(f"{rouge}Niveau de la machine invalide.{reset}")
        niveau_machine1 = int(input(f"  Votre choix \n{jaune} -> {reset}"))

    print("  Veuillez choisir le niveau de la machine 2 :")
    print("\t1. Niveau 1")
    print("\t2. Niveau 2")
    print("\t3. Niveau 3")
    niveau_machine2: int
    niveau_machine2 = int(input(f"  Votre choix \n{jaune} -> {reset}"))
    while niveau_machine2 != 1 and niveau_machine2 != 2 and niveau_machine2 != 3:
        print(f"{rouge}Niveau de la machine invalide.{reset}")
        niveau_machine2 = int(input(f"  Votre choix \n{jaune} -> {reset}"))

    print()
    tours: int
    tours = int(input(f"  Veuillez choisir le nombre de tour de jeu \n{jaune} -> {reset}"))

    boucle_machine_vs_machine_morpion(niveau_machine1, niveau_machine2, tours)
    