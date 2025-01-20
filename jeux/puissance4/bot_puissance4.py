from jeux.puissance4.joueur_puissance4 import verifier_colonne_pleine, trouver_ligne_vide, verifier_victoire, verifier_match_nul, titre_puissance4, afficher_grille, coup_joueur, placer_jeton_animation, fin_jeu_joueur, placer_jeton
from base.outils import jaune, reset, passer, rouge, gris, orange
from base.interface_joueurs import Interface
import random, time


def coup_machine_n1(grille: list[list[str]]) -> int:
    """
    Niveau 1: Choix aléatoire d'une colonne non pleine.

    Args:
        grille (list[list[str]]): La grille de jeu.

    Returns:
        int: L'indice de la colonne choisie.
    """
    colonne_valides: list[int]
    colonnes_valides = [col for col in range(7) if not verifier_colonne_pleine(grille, col)]
    return random.choice(colonnes_valides)


def coup_machine_n2(grille: list[list[str]]) -> int:
    """
    Niveau 2: Choix aléatoire avec une légère préférence pour le centre.

    Args:
        grille (list[list[str]]): La grille de jeu.

    Returns:
        int: L'indice de la colonne choisie.
    """
    colonne_valides: list[int]
    colonnes_valides = [col for col in range(7) if not verifier_colonne_pleine(grille, col)]
    if 3 in colonnes_valides:
        return 3
    return random.choice(colonnes_valides)


def coup_machine_n3(grille: list[list[str]]) -> int:
    """
    Niveau 3: Stratégie gagnante.

    Args:
        grille (list[list[str]]): La grille de jeu.

    Returns:²
        int: L'indice de la colonne choisie.
    """
    # Vérifier si le bot peut gagner au prochain coup
    col: int
    ligne: int
    colonne_valides: list[int]
    for col in range(7):
        if not verifier_colonne_pleine(grille, col):
            ligne = trouver_ligne_vide(grille, col)
            grille[ligne][col] = '🔴'
            if verifier_victoire(grille):
                grille[ligne][col] = '  '
                return col
            grille[ligne][col] = '  '

    # Vérifier si l'adversaire peut gagner au prochain coup et bloquer
    for col in range(7):
        if not verifier_colonne_pleine(grille, col):
            ligne = trouver_ligne_vide(grille, col)
            grille[ligne][col] = '🟡'
            if verifier_victoire(grille):
                grille[ligne][col] = '  '
                return col
            grille[ligne][col] = '  '

    # Sinon, choisir une colonne aléatoire
    colonnes_valides = [col for col in range(7) if not verifier_colonne_pleine(grille, col)]
    return random.choice(colonnes_valides)


def coup_machine(grille: list[list[str]], niveau: int) -> int:
    """
    Choisit un coup pour la machine en fonction du niveau.

    Args:
        grille (list[list[str]]): La grille de jeu.
        niveau (int): Le niveau de la machine.

    Returns:
        int: L'indice de la colonne choisie.
    """
    if niveau == 1:
        return coup_machine_n1(grille)
    elif niveau == 2:
        return coup_machine_n2(grille)
    return coup_machine_n3(grille)


def fin_jeu_bot(grille: list[list[str]], niveau: int, signe: str) -> None:
    """
    Gère la fin de jeu pour le bot.

    Args:
        grille (list[list[str]]): La grille de jeu.
        niveau (int): Le niveau de la machine.
        signe (str): Le signe du bot.

    Returns:
        None
    """
    if verifier_victoire(grille):
        print(f"\nLe bot de niveau {niveau} ({signe}) a gagné !")
    if verifier_match_nul(grille):
        print(f"\n\t{jaune}Match nul !{reset}")


def gestion_joueur_vs_bot(interface: Interface, niveau: int) -> None:
    """
    Gère une partie entre un joueur et un bot.

    Args:
        interface (Interface): L'interface contenant les joueurs.
        niveau (int): Le niveau de la machine.

    Returns:
        None
    """
    grille: list[list[str]]
    grille = [['  ' for _ in range(7)] for _ in range(6)]

    joueur_actif: int
    joueur_actif = random.choice([interface.indice_joueur1, -1])
    signe_actif: str
    signe_actif = '🔴'

    while not verifier_victoire(grille) and not verifier_match_nul(grille):
        titre_puissance4()
        afficher_grille(grille)

        colonne: int
        if joueur_actif == interface.indice_joueur1:
            colonne = coup_joueur(interface, joueur_actif, signe_actif, grille)
        else:
            colonne = coup_machine(grille, niveau)

        ligne: int
        ligne = trouver_ligne_vide(grille, colonne)

        placer_jeton_animation(grille, signe_actif, colonne, ligne)

        if joueur_actif == interface.indice_joueur1:
            fin_jeu_joueur(interface, grille, joueur_actif, signe_actif)
        else:
            fin_jeu_bot(grille, niveau, signe_actif)

        joueur_actif = interface.indice_joueur1 if joueur_actif == -1 else -1
        signe_actif = '🔴' if signe_actif == '🟡' else '🟡'

    print()
    passer()


def joueur_vs_bot(interface: Interface) -> None:
    """
    Permet de jouer une partie contre un bot.

    Args:
        interface (Interface): L'interface contenant les joueurs.

    Returns:
        None
    """
    titre_puissance4()

    print("  Veuillez choisir le niveau de la machine :")
    print("\t1. Niveau 1")
    print("\t2. Niveau 2")
    print("\t3. Niveau 3")
    niveau_machine: int
    niveau_machine = int(input(f"Votre choix \n{jaune} -> {reset}"))
    while niveau_machine != 1 and niveau_machine != 2 and niveau_machine != 3:
        print(f"{rouge}Niveau de la machine invalide.{reset}")
        niveau_machine = int(input(f"Votre choix \n{jaune} -> {reset}"))
    gestion_joueur_vs_bot(interface, niveau_machine)


def gestion_bot_vs_bot(niveau_machine1: int, niveau_machine2: int) -> int:
    """
    Gère une partie entre deux bots.

    Args:
        niveau_machine1 (int): Le niveau de la première machine.
        niveau_machine2 (int): Le niveau de la deuxième machine.

    Returns:
        int: Le numéro du bot gagnant, ou 0 en cas de match nul.
    """
    grille: list[list[str]]
    grille = [['  ' for _ in range(7)] for _ in range(6)]

    bot_actif: int
    bot_actif = random.choice([1, 2])
    signe_actif: str
    signe_actif = '🔴'
    niveau_actif = niveau_machine1 if bot_actif == 1 else niveau_machine2

    while not verifier_victoire(grille) and not verifier_match_nul(grille):
        colonne: int
        if bot_actif == 1:
            colonne = coup_machine(grille, niveau_machine1)
        else:
            colonne = coup_machine(grille, niveau_machine2)

        ligne: int
        ligne = trouver_ligne_vide(grille, colonne)

        placer_jeton(grille, signe_actif, colonne, ligne)

        print(f"Jeu de la machine n°{bot_actif} ({signe_actif}) de niveau {niveau_actif}")
        afficher_grille(grille)

        print()
        print(f"{gris}-{reset}" * 85)
        print()

        fin_jeu_bot(grille, niveau_actif, signe_actif)

        bot_actif = 1 if bot_actif == 2 else 2
        signe_actif = '🔴' if signe_actif == '🟡' else '🟡'
        niveau_actif = niveau_machine1 if bot_actif == 1 else niveau_machine2

    bot_actif = 1 if bot_actif == 2 else 2
    if verifier_victoire(grille):
        return bot_actif
    return 0


def gestion_boucle_bot_vs_bot(niveau_machine1: int, niveau_machine2: int, tours: int) -> None:
    """
    Gère une série de parties entre deux bots.

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

    titre_puissance4()
    for _ in range(tours):
        res = gestion_bot_vs_bot(niveau_machine1, niveau_machine2)
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


def bot_vs_bot() -> None:
    """
    Permet de jouer une série de parties entre deux bots.

    Returns:
        None
    """
    titre_puissance4()

    print("  Veuillez choisir le niveau de la machine 1 :")
    print("\t1. Niveau 1")
    print("\t2. Niveau 2")
    print("\t3. Niveau 3")
    niveau_machine1: int
    niveau_machine1 = int(input(f"Votre choix \n{jaune} -> {reset}"))
    while niveau_machine1 != 1 and niveau_machine1 != 2 and niveau_machine1 != 3:
        print(f"{rouge}Niveau de la machine invalide.{reset}")
        niveau_machine1 = int(input(f"Votre choix \n{jaune} -> {reset}"))

    print("  Veuillez choisir le niveau de la machine 2 :")
    print("\t1. Niveau 1")
    print("\t2. Niveau 2")
    print("\t3. Niveau 3")
    niveau_machine2: int
    niveau_machine2 = int(input(f"Votre choix \n{jaune} -> {reset}"))
    while niveau_machine2 != 1 and niveau_machine2 != 2 and niveau_machine2 != 3:
        print(f"{rouge}Niveau de la machine invalide.{reset}")
        niveau_machine2 = int(input(f"Votre choix \n{jaune} -> {reset}"))

    print()
    tours: int
    tours = int(input(f"  Veuillez choisir le nombre de tour de jeu \n{jaune} -> {reset}"))

    gestion_boucle_bot_vs_bot(niveau_machine1, niveau_machine2, tours)