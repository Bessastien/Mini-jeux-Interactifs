import pickle
from typing import BinaryIO
from base.interface_joueurs import Interface, Joueur
from base.outils import *


def sauvegarder_interface(interface: Interface) -> None:
    f: BinaryIO
    clear()
    print("Sauvegarde de l'interface...")
    j: list[Joueur]
    j = []
    sauv: tuple[list[Joueur], int]
    long: int
    long = interface.longueur
    for joueur in interface.joueurs:
        j.append(joueur)
    sauv = (j, long)
    f = open('base/interface.dat', 'wb')
    pickle.dump(sauv, f)


def charger_interface() -> Interface:
    f: BinaryIO
    try:
        f = open('base/interface.dat', 'rb')
        interface: Interface
        interface = Interface()
        sauv = pickle.load(f)
        print(sauv)
        interface.joueurs = sauv[0]
        interface.longueur = sauv[1]
        print("Chargement de l'interface...")
        return interface
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée, création d'une nouvelle interface.")
        return Interface()


def reset_interface(interface: Interface) -> None:
    choix: str
    choix = input(f" {rouge}ATTENTION{reset} | Voulez-vous vraiment supprimer la sauvegarde ? (o/n) : ")

    if choix == 'o':
        interface.joueurs = []
        interface.indice_joueur1 = -1
        interface.indice_joueur2 = -1
        interface.longueur = 0
        f: BinaryIO
        f = open('base/interface.dat', 'wb')
        pickle.dump(([], 0), f)
        print(f"{rouge}Sauvegarde supprimée.{reset}")
