from jeux.devinette.joueur_devinette import titre_devinette, premiere_etape, deuxieme_etape
from base.interface_joueurs import Interface, get_name, ajouter_score_devinette
from base.outils import attendre, passer, rouge, reset, gris, jaune, vert, orange, bleu
from random import choice, randint
from time import time


# Fonctions pour la machine
# Choix du nombre par la machine
def choix_machine_n1(maximum: int) -> int:
    """
    Cette fonction permet à la machine de choisir un nombre entre 1 et maximum. (Niveau 1)
    Elle choisit la moitié ou un quart de la plage.
    Args:
        maximum (int): Le nombre maximum que la machine peut choisir.

    Returns:
        int: Le nombre choisi par la machine.
    """
    choix: int
    choix = choice([maximum//2, maximum//4, maximum//4+maximum//2])
    return choix


def choix_machine_n2(maximum: int) -> int:
    """
    Cette fonction permet à la machine de choisir un nombre entre 1 et maximum. (Niveau 2)
    Elle choisit un nombre aléatoire entre 1 et maximum.
    Choisit un nombre aleatoire.

    Args:
        maximum (int): Le nombre maximum que la machine peut choisir.

    Returns:
        int: Le nombre choisi par la machine.
    """
    return randint(1, maximum)


# coup par coup pour deviner le nombre
def coup_suivant_n1(maximum: int) -> int:
    """
    Cette fonction permet à la machine de choisir un nombre entre 1 et maximum. (Niveau 1)
    Elle choisit un nombre aléatoire entre 1 et maximum.

    Args:
        maximum (int): Le nombre maximum que la machine peut choisir.

    Returns:
        int: Le nombre choisi par la machine.
    """
    return randint(1, maximum)


def coup_suivant_n2(debut: int, fin: int) -> int:
    """
    Cette fonction permet à la machine de choisir un nombre entre debut et fin. (Niveau 2)

    Args:
        debut (int): Le début de la plage de nombres.
        fin (int): La fin de la plage de nombres.

    Returns:
        int: Le nombre choisi par la machine.
    """
    return randint(debut, fin)


def coup_suivant_n3(debut: int, fin: int) -> int:
    """
    Cette fonction permet à la machine de choisir un nombre entre debut et fin. (Niveau 3)
    Elle choisit le nombre au milieu de la plage.

    Args:
        debut (int): Le début de la plage de nombres.
        fin (int): La fin de la plage de nombres.

    Returns:
        int: Le nombre choisi par la machine.
    """
    return (fin - debut) // 2 + debut


def choix_machine(niveau_machine: int, maximum: int, debut: int, fin: int) -> int:
    """
    Cette fonction permet à la machine de choisir un nombre en fonction de son niveau.

    Args:
        niveau_machine (int): Le niveau de la machine.
        maximum (int): Le nombre maximum que la machine peut choisir.
        debut (int): Le début de la plage de nombres.
        fin (int): La fin de la plage de nombres.

    Returns:
        int: Le nombre choisi par la machine.
    """
    if niveau_machine == 1:
        return coup_suivant_n1(maximum)
    elif niveau_machine == 2:
        return coup_suivant_n2(debut, fin)
    elif niveau_machine == 3:
        return coup_suivant_n3(debut, fin)
    else:
        print(f"{rouge}Niveau de la machine invalide.{reset}")
        attendre()
        return 1


def premiere_etape_bot(maximum: int, niveau_machine: int) -> int:
    """
    Cette fonction permet à la machine de choisir un nombre en fonction de son niveau pour la première étape.

    Args:
        maximum (int): Le nombre maximum que la machine peut choisir.
        niveau_machine (int): Le niveau de la machine.

    Returns:
        int: Le nombre choisi par la machine.
    """
    nombre: int
    nombre = 1
    if niveau_machine == 1:
        nombre = choix_machine_n1(maximum)
    elif niveau_machine == 2:
        nombre = choix_machine_n2(maximum)
    else:
        print(f"{rouge}Niveau de la machine invalide.{reset}")
        attendre()
    return nombre


def deuxieme_etape_bot(maximum: int, tentative: int, nombre_a_deviner: int, niveau_machine: int) -> tuple[int, int]:
    """
    Cette fonction permet à la machine de deviner un nombre en fonction de son niveau pour la deuxième étape.

    Args:
        maximum (int): Le nombre maximum que la machine peut choisir.
        tentative (int): Le nombre de tentatives de la machine.
        nombre_a_deviner (int): Le nombre que la machine doit deviner.
        niveau_machine (int): Le niveau de la machine.

    Returns:
        tuple[int, int]: La proposition de la machine et le nombre d'essais effectués.
    """
    print(f"\n  La machine à {tentative} essais pour trouver le nombre compris entre 1 et {maximum} compris.\n")

    essais: int
    essais = 0
    proposition: int
    proposition = 0
    debut: int
    fin: int
    debut = 1
    fin = maximum

    while proposition != nombre_a_deviner and essais != tentative:
        proposition = choix_machine(niveau_machine, maximum, debut, fin)
        print(f"  Tentative n°{bleu}{essais + 1}{reset} :")
        print(f"\tLa machine propose le nombre {orange}{proposition}{reset}.")
        essais += 1
        if proposition < nombre_a_deviner:
            debut = proposition + 1
        elif proposition > nombre_a_deviner:
            fin = proposition - 1

    return proposition, essais


def JoueurVSMachineCherche(interface: Interface, niveau_machine: int, maximum: int, tentative: int):
    """
    Cette fonction permet de jouer une partie où le joueur choisit un nombre et la machine doit le deviner.

    Args:
        interface (Interface): L'interface contenant les joueurs.
        maximum (int): Le nombre maximum que la machine peut choisir.
        niveau_machine (int): Le niveau de la machine.
        tentative (int): Le nombre de tentatives de la machine.

    Returns:
        None
    """
    indice: int
    indice = interface.indice_joueur1
    pseudo: str
    pseudo = get_name(interface, indice)

    # Premiere étape : choix du nombre
    nombre_a_deviner = premiere_etape(maximum, pseudo)

    # Deuxième étape : devinette
    fin: tuple[int, int]
    titre_devinette()
    fin = deuxieme_etape_bot(maximum, tentative, nombre_a_deviner, niveau_machine)
    proposition: int
    proposition = fin[0]
    essais: int
    essais = fin[1]

    print()
    print(f"{gris}-{reset}" * 85)
    print()

    # Fin du jeu
    if proposition == nombre_a_deviner:
        print(f"Dommage {rouge}{pseudo}{reset} ! la machine avait choisi le nombre {nombre_a_deviner} et l'a trouvé en {essais} essais.")
    else:
        print(f"Bravo {vert}{pseudo}{reset} ! La machine n'a pas trouvé le nombre {nombre_a_deviner}.")
        ajouter_score_devinette(interface, indice, 1)
    print("\n")
    print(f"{gris}={reset}" * 85)
    print()
    passer()


def MachineVSJoueurCherche(interface: Interface, niveau_machine: int, maximum: int, tentative: int):
    """
    Cette fonction permet de jouer une partie où la machine choisit un nombre et le joueur doit le deviner.

    Args:
        interface (Interface): L'interface contenant les joueurs.
        niveau_machine (int): Le niveau de la machine.
        maximum (int): Le nombre maximum que la machine peut choisir.
        tentative (int): Le nombre de tentatives du joueur.

    Returns:
        None
    """
    indice: int
    indice = interface.indice_joueur1
    pseudo: str
    pseudo = get_name(interface, indice)

    # Premiere étape : choix du nombre
    nombre: int
    nombre = premiere_etape_bot(maximum, niveau_machine)

    # Deuxième étape : devinette
    titre_devinette()
    fin: tuple[int, int]
    fin = deuxieme_etape(maximum, tentative, pseudo, nombre)
    proposition: int
    proposition = fin[0]
    essais: int
    essais = fin[1]

    # Fin du jeu
    if proposition == nombre:
        print(f"  Bravo {vert}{pseudo}{reset} ! Vous avez trouvé le nombre {nombre} en {essais} essais.")
        ajouter_score_devinette(interface, indice, 1)
    else:
        print(f"  Dommage {rouge}{pseudo}{reset} ! la machine a trouvé le nombre {nombre} en {essais} essaisq.")
    print("\n")
    print(f"{gris}={reset}" * 85)
    print()
    passer()


def JoueurVSMachine(interface: Interface, maximum: int, tentative: int):
    """
    Cette fonction permet de jouer une partie où le joueur choisit un nombre et la machine doit le deviner, ou vice versa.

    Args:
        interface (Interface): L'interface contenant les joueurs.
        maximum (int): Le nombre maximum que la machine peut choisir.
        tentative (int): Le nombre de tentatives de la machine ou du joueur.

    Returns:
        None
    """
    titre_devinette()

    print("Qui doit deviner le nombre ?")
    print("\t1. La machine")
    print("\t2. Vous")
    choix: int
    choix = int(input(f"Votre choix \n{jaune} -> {reset}"))
    while choix != 1 and choix != 2:
        print(f"{rouge}Veuillez entrer 1 ou 2.{reset}")
        choix = int(input(f"Votre choix \n{jaune} -> {reset}"))

    print()

    if choix == 1:
        print("Veuillez choisir le niveau de la machine :")
        print("\t1. Niveau 1")
        print("\t2. Niveau 2")
        print("\t3. Niveau 3")
        niveau_machine: int
        niveau_machine = int(input(f"Votre choix \n{jaune} -> {reset}"))
        while niveau_machine != 1 and niveau_machine != 2 and niveau_machine != 3:
            print(f"{rouge}Niveau de la machine invalide.{reset}")
            niveau_machine = int(input(f"Votre choix \n{jaune} -> {reset}"))
    else :
        print("Veuillez choisir le niveau de la machine :")
        print("\t1. Niveau 1")
        print("\t2. Niveau 2")
        niveau_machine: int
        niveau_machine = int(input(f"Votre choix \n{jaune} -> {reset}"))
        while niveau_machine != 1 and niveau_machine != 2:
            print(f"{rouge}Niveau de la machine invalide.{reset}")
            niveau_machine = int(input(f"Votre choix \n{jaune} -> {reset}"))

    if choix == 1:
        JoueurVSMachineCherche(interface, niveau_machine, maximum, tentative)
    elif choix == 2:
        MachineVSJoueurCherche(interface, niveau_machine, maximum, tentative)


def MachineVSMachine(niveau_machine1: int, niveau_machine2: int, maximum: int, tentative: int):
    """
    Cette fonction permet de jouer une partie où deux machines s'affrontent pour deviner un nombre.

    Args:
        niveau_machine1 (int): Le niveau de la machine qui choisit le nombre.
        niveau_machine2 (int): Le niveau de la machine qui devine le nombre.
        maximum (int): Le nombre maximum que la machine peut choisir.
        tentative (int): Le nombre de tentatives de la machine.

    Returns:
        int: Le résultat de la partie (1 si la machine 1 gagne, 2 si la machine 2 gagne).
    """
    # Premiere étape : choix du nombre
    nombre: int
    nombre = premiere_etape_bot(maximum, niveau_machine1)
    print(f"  La machine a choisi le nombre {nombre}.\n")
    print(f"{gris}-{reset}" * 85)

    # Deuxième étape : devinette
    fin: tuple[int, int]
    fin = deuxieme_etape_bot(maximum, tentative, nombre, niveau_machine2)
    proposition: int
    proposition = fin[0]
    essais: int
    essais = fin[1]

    print()
    print(f"{gris}-{reset}" * 85)
    print()

    # Fin du jeu
    if proposition == nombre:
        print(f"{vert}La machine qui devait trouver le nombre l'a trouvé en {essais} essais.{reset}")
        return 2
    else:
        print(f"{rouge}La machine qui devait trouver le nombre n'a pas réussi.{reset}")
        return 1


def gestion_boucle_MachineVSMachine(niveau_machine1: int, niveau_machine2: int, maximum: int, tentative: int, nombres_de_tours: int):
    """
    Cette fonction permet de gérer une série de parties où deux machines s'affrontent pour deviner un nombre.

    Args:
        niveau_machine1 (int): Le niveau de la machine qui choisit le nombre.
        niveau_machine2 (int): Le niveau de la machine qui devine le nombre.
        maximum (int): Le nombre maximum que la machine peut choisir.
        tentative (int): Le nombre de tentatives de la machine.
        nombres_de_tours (int): Le nombre de tours à jouer.

    Returns:
        None
    """
    score_machine1: int
    score_machine1 = 0
    score_machine2: int
    score_machine2 = 0

    start: float
    start = time()

    for _ in range(nombres_de_tours):
        res = MachineVSMachine(niveau_machine1, niveau_machine2, maximum, tentative)
        if res == 1:
            score_machine1 += 1
        else:
            score_machine2 += 1

        print()
        print(f"{gris}={reset}" * 85)
        print()

    print(f"{orange}Fin de la partie !{reset}")
    print()
    temps: float
    temps = time() - start
    temps = round(temps, 2)

    print(f"Score de la machine 1 (fait deviner le nombre) : {score_machine1}")
    print(f"Score de la machine 2 (devine le nombre) : {score_machine2}")
    print(f"Temps de l'exécution du programme : {temps} secondes")
    print()
    passer()


def boucle_MachineVSMachine(maximum: int, tentative: int):
    """
    Cette fonction permet de jouer une série de parties où deux machines s'affrontent pour deviner un nombre.

    Args:
        maximum (int): Le nombre maximum que la machine peut choisir.
        tentative (int): Le nombre de tentatives de la machine.

    Returns:
        None
    """
    titre_devinette()

    print("  Veuillez choisir le niveau de la machine qui fait deviner le nombre :")
    print("\t1. Niveau 1")
    print("\t2. Niveau 2")
    niveau_machine1: int
    niveau_machine1 = 0
    while niveau_machine1 != 1 and niveau_machine1 != 2:
        niveau_machine1 = int(input(f"  Votre choix \n{jaune} -> {reset}"))

    print()

    print("  Veuillez choisir le niveau de la machine qui devine le nombre :")
    print("\t1. Niveau 1")
    print("\t2. Niveau 2")
    print("\t3. Niveau 3")
    niveau_machine2: int
    niveau_machine2 = 0
    while niveau_machine2 != 1 and niveau_machine2 != 2 and niveau_machine2 != 3:
        niveau_machine2 = int(input(f"  Votre choix \n{jaune} -> {reset}"))

    print()

    nombres_de_tours: int
    nombres_de_tours = int(input(f"Combien de tours voulez-vous jouer ? \n{jaune} -> {reset}"))

    gestion_boucle_MachineVSMachine(niveau_machine1, niveau_machine2, maximum, tentative, nombres_de_tours)
