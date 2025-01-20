from base.outils import *
from base.interface_joueurs import *
from jeux.allumette.joueur_allumette import *
import random, time


def machine_n1(nombre_allumettes: int) -> int:
    """
    Niveau 1 : Retire un nombre aléatoire d'allumettes.

    Ce bot joue sans réflexion stratégique. Il retire un nombre aléatoire
    d'allumettes compris entre 1 et le minimum de 3 et du nombre
    total d'allumettes disponibles.

    Args:
        nombre_allumettes (int): Nombre d'allumettes restantes dans le jeu.

    Returns:
        int: Le nombre d'allumettes retirées (entre 1 et 3).
    """
    return random.randint(1, min(3, nombre_allumettes))


def machine_n3(nombre_allumettes: int) -> int:
    """
    Niveau 3 : Joue de manière optimale, en forçant l'adversaire à prendre la dernière allumette.

    Ce bot utilise une stratégie mathématique optimale. Il tente toujours
    de laisser à l'adversaire un nombre d'allumettes où le total - 1
    est un multiple de 4. Cela garantit que l'adversaire se retrouve
    dans une position perdante, sauf cas initialement désavantageux.

    En cas de position déjà désavantageuse pour lui
    (où nombre_allumettes - 1 est un multiple de 4), le bot jouera
    de manière aléatoire entre 1 et 3 allumettes.

    Args:
        nombre_allumettes (int): Nombre d'allumettes restantes dans le jeu.

    Returns:
        int: Le nombre d'allumettes retirées (entre 1 et 3).
    """
    if (nombre_allumettes - 1) % 4 == 0:
        return random.randint(1, min(3, nombre_allumettes))

    coup: int
    coup = (nombre_allumettes - 1) % 4
    if coup == 0:
        coup = random.randint(1, min(3, nombre_allumettes))
    return min(max(1, coup), 3)


def machine_n2(nombre_allumettes: int) -> int:
    """
    Niveau 2 : Joue de manière semi-stratégique pour éviter de prendre la dernière allumette.

    Le bot a une chance sur 2 de jouer de manière optimale ou de jouer aléatoirement

    Args:
        nombre_allumettes (int): Nombre d'allumettes restantes dans le jeu.

    Returns:
        int: Le nombre d'allumettes retirées (entre 1 et 3).
    """
    return random.choice([machine_n1(nombre_allumettes), machine_n3(nombre_allumettes)])


def resultat_machine(nombres_allumettes: int, niveau: int) -> int:
    """
    Fonction qui permet à la machine de jouer.

    Args:
        nombres_allumettes (int): Le nombre d'allumettes restantes.
        niveau (int): Le niveau de la machine.

    Returns:
        int: Le nombre d'allumettes à retirer.
    """
    if niveau == 1:
        return machine_n1(nombres_allumettes)
    elif niveau == 2:
        return machine_n2(nombres_allumettes)
    return machine_n3(nombres_allumettes)


def tour_bot_allumette(niveau: int, nombre_allumette: int) -> int:
    """
    Fonction qui permet au bot de jouer.

    Args:
        niveau (int): Le niveau du bot.
        nombre_allumette (int): Le nombre d'allumettes restantes.

    Returns:
        int: Le nombre d'allumettes restantes.
    """
    allumette_a_retirer: int
    allumette_a_retirer = resultat_machine(nombre_allumette, niveau)
    print(f"\n  Le bot de niveau {niveau} retire {allumette_a_retirer} allumettes.")
    return nombre_allumette - allumette_a_retirer


def gestion_joueur_vs_machine_allumette(interface: Interface, niveau: int) -> None:
    """
    Fonction qui permet de gérer le jeu entre un joueur et la machine.

    Args:
        interface(Interface): L'interface contenant les joueurs.
        niveau(int): Le niveau de la machine.

    Returns:
        None
    """
    nombres_allumettes: int
    nombres_allumettes = 20

    indice_joueur_actif: int
    indice_joueur_actif = random.choice([interface.indice_joueur1, -1])

    titre_allumette()
    if indice_joueur_actif == -1:
        print(f"\t{bleu}La machine commence la partie !{reset}\n")
    else:
        print(f"\t{bleu}{get_name(interface, indice_joueur_actif)}{reset} commence la partie !\n")
    print(f"{gris}-{reset}" * 85)
    print()
    attendre()

    while nombres_allumettes > 0:

        print(f"\tIl reste {rouge}{nombres_allumettes}{reset} allumettes.")

        if indice_joueur_actif == -1:
            nombres_allumettes = tour_bot_allumette(niveau, nombres_allumettes)
            indice_joueur_actif = interface.indice_joueur1
        else:
            nombres_allumettes = tour_joueur_allumette(interface, nombres_allumettes, indice_joueur_actif)
            indice_joueur_actif = -1

        print()
        print(f"{gris}-{reset}" * 85)
        print()

        # Vérification de la fin de partie
        if nombres_allumettes == 0:
            if indice_joueur_actif == -1:
                print(f"\t{rouge}La machine de niveau {niveau} à gagné !{reset}")
            else:
                print(f"\t{bleu}{get_name(interface, indice_joueur_actif)}{reset} a gagné !")
                ajouter_score_allumette(interface, indice_joueur_actif, 1)

            print()
            print(f"{gris}={reset}" * 85)
            passer()


def joueur_vs_machine_allumette(interface: Interface) -> None:
    """
    Fonction qui permet de jouer contre la machine.

    Args:
        interface (Interface): L'interface contenant les joueurs.

    Returns:
        None
    """
    niveau: int
    niveau = 0

    titre_allumette()

    while niveau < 1 or niveau > 3:
        niveau = int(input(f"\n  Choisissez le niveau de la machine (1, 2 ou 3) \n{jaune} -> {reset} "))
        if niveau < 1 or niveau > 3:
            print(f"\n\t{rouge}Choix invalide.{reset}")

    gestion_joueur_vs_machine_allumette(interface,niveau)


def gestion_machine_vs_machine_allumette(niveau1: int, niveau2: int) -> int:
    """
    Cette fonction permet de gérer le jeu entre deux machines.

    Args:
        niveau1(int): Le niveau de la première machine.
        niveau2(int): Le niveau de la deuxième machine.

    Returns:
        int: L'indice du bot Gagnant.
    """
    nombres_allumettes: int
    nombres_allumettes = 20
    indice_bot_actif: int
    indice_bot_actif = random.choice([1,2])

    print(f"  Les machines vont s'affronter !")

    print()
    print(f"{gris}-{reset}" * 85)
    print()

    while nombres_allumettes > 0:

        print(f"\tIl reste {rouge}{nombres_allumettes}{reset} allumettes.")

        if indice_bot_actif == 1:
            nombres_allumettes = tour_bot_allumette(niveau1, nombres_allumettes)
            indice_bot_actif = 2
        else:
            nombres_allumettes = tour_bot_allumette(niveau2, nombres_allumettes)
            indice_bot_actif = 1

        print()
        print(f"{gris}-{reset}" * 85)
        print()

        # Vérification de la fin de partie
        if nombres_allumettes == 0:
            if indice_bot_actif == 1:
                print(f"\n\t{rouge}La machine de niveau {niveau1} à gagné !{reset}")
            else:
                print(f"\n\t{rouge}La machine de niveau {niveau2} à gagné !{reset}")

            print()
            print(f"{gris}={reset}" * 85)
            print()

    return indice_bot_actif


def machine_vs_machine_allumette() -> None:
    """
    Cette fonction permet faire jouer deux machines.

    Returns:
        None
    """
    niveau1: int
    niveau1 = 0
    niveau2: int
    niveau2 = 0
    tours: int
    tours = 0
    score_bot1: int
    score_bot1 = 0
    score_bot2: int
    score_bot2 = 0

    titre_allumette()

    while niveau1 < 1 or niveau1 > 3:
        niveau1 = int(input(f"\n  Choisissez le niveau de la première machine (1, 2 ou 3) \n{jaune} -> {reset} "))
        if niveau1 < 1 or niveau1 > 3:
            print(f"\n\t{rouge}Choix invalide.{reset}")

    while niveau2 < 1 or niveau2 > 3:
        niveau2 = int(input(f"\n  Choisissez le niveau de la deuxième machine (1, 2 ou 3) \n{jaune} -> {reset} "))
        if niveau2 < 1 or niveau2 > 3:
            print(f"\n\t{rouge}Choix invalide.{reset}")

    while tours <= 0:
        tours = int(input(f"\n  Combien de tours voulez-vous jouer ?\n{jaune} -> {reset} "))
        if tours < 0:
            print(f"\n\t{rouge}Choix invalide.{reset}")

    start: float
    start = time.time()
    for i in range(tours):
        gagnant = gestion_machine_vs_machine_allumette(niveau1,niveau2)
        if gagnant == 1:
            score_bot1 += 1
        else:
            score_bot2 += 1

    temps: float
    temps = time.time() - start
    temps = round(temps, 2)
    print(f"\n\t{bleu}Score final :{reset}")
    print(f"  Machine de niveau {niveau1} : {score_bot1} victoires")
    print(f"  Machine de niveau {niveau2} : {score_bot2} victoires")
    print(f"Temps de l'exécution du programme : {temps} secondes")
    print()
    passer()


