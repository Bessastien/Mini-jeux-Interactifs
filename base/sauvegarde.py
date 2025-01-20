import pickle
from typing import BinaryIO
from base.interface_joueurs import Interface, Joueur
from base.outils import clear, rouge, reset


def sauvegarder_interface(interface: Interface) -> None:
    """
    Sauvegarde l'état actuel de l'interface dans un fichier binaire.

    Args:
        interface (Interface): L'interface contenant les joueurs à sauvegarder.

    Returns:
        None
    """
    f: BinaryIO
    clear()  # Nettoie la console
    print("Sauvegarde de l'interface...")
    j: list[Joueur]
    j = []  # Liste pour stocker les joueurs
    sauv: tuple[list[Joueur], int]
    long: int
    long = interface.longueur  # Longueur actuelle de la liste des joueurs
    for joueur in interface.joueurs:
        j.append(joueur)  # Ajoute chaque joueur à la liste
    sauv = (j, long)  # Crée un tuple avec la liste des joueurs et la longueur
    f = open('base/interface.dat', 'wb')  # Ouvre le fichier en mode binaire pour écriture
    pickle.dump(sauv, f)  # Sauvegarde le tuple dans le fichier


def charger_interface() -> Interface:
    """
    Charge l'état de l'interface à partir d'un fichier binaire.

    Returns:
        Interface: L'interface chargée depuis le fichier de sauvegarde.
    """
    f: BinaryIO
    try:
        f = open('base/interface.dat', 'rb')  # Ouvre le fichier en mode binaire pour lecture
        interface: Interface
        interface = Interface()  # Crée une nouvelle instance de l'interface
        sauv = pickle.load(f)  # Charge les données du fichier
        print(sauv)
        interface.joueurs = sauv[0]  # Récupère la liste des joueurs
        interface.longueur = sauv[1]  # Récupère la longueur de la liste des joueurs
        print("Chargement de l'interface...")
        return interface
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée, création d'une nouvelle interface.")
        return Interface()  # Retourne une nouvelle instance de l'interface si le fichier n'existe pas


def reset_interface(interface: Interface) -> None:
    """
    Réinitialise l'interface et supprime la sauvegarde existante.

    Args:
        interface (Interface): L'interface à réinitialiser.

    Returns:
        None
    """
    choix: str
    choix = input(f" {rouge}ATTENTION{reset} | Voulez-vous vraiment supprimer la sauvegarde ? (o/n) : ")

    if choix == 'o':
        interface.joueurs = []
        interface.indice_joueur1 = -1
        interface.indice_joueur2 = -1
        interface.longueur = 0
        f: BinaryIO
        f = open('base/interface.dat', 'wb')  # Ouvre le fichier en mode binaire pour écriture
        pickle.dump(([], 0), f)  # Sauvegarde une liste vide et une longueur de 0 dans le fichier
        print(f"{rouge}Sauvegarde supprimée.{reset}")