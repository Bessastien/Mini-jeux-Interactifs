import time
from base.interface_joueurs import Interface, recup_joueur1, recup_joueur2, get_name, ajouter_score_devinette
from base.outils import clear, attendre, passer, gris, jaune, rouge, bleu, magenta, reset
from base.outils import clear, attendre, passer, gris, jaune, rouge, bleu, magenta, reset


def titre_devinette() -> None:
    """
    Affiche le titre du jeu de devinette.

    Returns:
        None
    """
    clear()
    print(f"{gris}={reset}" * 85)
    print(" " * 35 + f"{jaune}Jeu de Devinette{reset}")
    print(f"{gris}={reset}" * 85)
    print("")


def qui_joue(interface: Interface) -> tuple[int, int]:
    """
    Demande à l'utilisateur de choisir qui va deviner le nombre et retourne les indices des joueurs.

    Args:
        interface (Interface): L'interface contenant les joueurs.

    Returns:
        tuple[int, int]: Les indices des joueurs (celui qui choisit le nombre, celui qui devine).
    """
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


def premiere_etape(maximum: int, pseudo: str) -> int:
    """
    Demande au joueur de choisir un nombre à deviner.

    Args:
        maximum (int): Le nombre maximum que le joueur peut choisir.
        pseudo (str): Le pseudo du joueur qui choisit le nombre.

    Returns:
        int: Le nombre choisi par le joueur.
    """
    titre_devinette()
    nombre_a_deviner: int
    nombre_a_deviner = int(input(f"\t{pseudo}, veuillez entrer un nombre entre 1 et {maximum} compris : "))
    while nombre_a_deviner < 1 or nombre_a_deviner > maximum:
        clear()
        titre_devinette()
        print(f"{rouge}Nombre invalide.{reset}\n")
        nombre_a_deviner = int(input(f"\t{pseudo}, veuillez entrer un nombre entre 1 et {maximum} compris : "))
    print("\n")
    print(f"{gris}-{reset}" * 85)
    print(f"\nVous avez choisi le nombre {bleu}{nombre_a_deviner}{reset} {magenta}(Message affiché 5s){reset}.\n\n")
    print(f"{gris}={reset}" * 85)
    time.sleep(5)
    clear()
    return nombre_a_deviner


def deuxieme_etape(maximum: int, tentative: int, pseudo: str, nombre_a_deviner: int) -> tuple[int, int]:
    """
    Permet au joueur de deviner le nombre choisi par l'autre joueur.

    Args:
        maximum (int): Le nombre maximum que le joueur peut choisir.
        tentative (int): Le nombre de tentatives autorisées.
        pseudo (str): Le pseudo du joueur qui devine.
        nombre_a_deviner (int): Le nombre à deviner.

    Returns:
        tuple[int, int]: La proposition du joueur et le nombre d'essais effectués.
    """
    titre_devinette()
    print(f"\t{pseudo}, c'est à vous de jouer !")
    print(f"  Vous avez {tentative} essais pour trouver le nombre compris entre 1 et {maximum} compris.\n")
    print(f"{gris}-{reset}" * 85)
    print()

    essais: int
    essais = 0
    proposition: int
    proposition = 0

    while proposition != nombre_a_deviner and essais != tentative:
        proposition = int(input(f"\n\tVeuillez entrer un nombre : "))
        if proposition == nombre_a_deviner:
            print("ah ?!")
        elif proposition < 1 or proposition > maximum:
            print(f"\n{rouge}Nombre invalide.{reset}")
        elif proposition < nombre_a_deviner:
            print(f"\nLe nombre est plus grand que {proposition}.")
        elif proposition > nombre_a_deviner:
            print(f"\nLe nombre est plus petit que {proposition}.")
        essais += 1
        print(f"Il vous reste {tentative - essais} essais.\n")
        print(f"{gris}-{reset}" * 85)
        print("\n")

    return proposition, essais


def jeu_devinette(interface: Interface, maximum: int, tentative: int) -> None:
    """
    Permet de jouer au jeu de devinette.

    Args:
        interface (Interface): L'interface contenant les joueurs.
        maximum (int): Le nombre maximum que le joueur peut choisir.
        tentative (int): Le nombre de tentatives autorisées.

    Returns:
        None
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

    # Premiere étape : choix du nombre
    nombre_a_deviner = premiere_etape(maximum, pseudo_j1)

    # Deuxieme étape : devinette
    fin: tuple[int, int]
    fin = deuxieme_etape(maximum, tentative, pseudo_j2, nombre_a_deviner)
    proposition: int
    proposition = fin[0]
    essais: int
    essais = fin[1]

    # Fin du jeu
    if proposition == nombre_a_deviner:
        print(f"Bravo {pseudo_j2} ! Vous avez trouvé le nombre {nombre_a_deviner} en {essais} essais.")
        ajouter_score_devinette(interface, indice_j2, 1)
    else:
        print(f"Dommage {pseudo_j2} ! le nombre était {nombre_a_deviner}.")
        ajouter_score_devinette(interface, indice_j1, 1)
    print("\n")
    print(f"{gris}={reset}" * 85)
    passer()
