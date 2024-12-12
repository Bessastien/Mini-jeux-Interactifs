from os import system, name
from time import sleep


def clear() -> None:
    """
    Cette fonction permet de nettoyer la console.
    Entrées : aucune
    Sorties : aucune
    """
    #windows
    if name == 'nt':
        _ = system('cls')
    #linux
    else:
        _ = system('clear')
    print()


def attendre() -> None:
    """
    Cette fonction permet de faire une pause.
    Entrées : aucune
    Sorties : aucune
    """
    sleep(1.2)


def passer() -> None:
    """
    Cette fonction permet de faire une pause.
    Entrées : aucune
    Sorties : aucune
    """
    input("Appuyez sur entrée pour continuer...")


#OUTILS DE COULEURS
jaune: str
gris: str
magenta: str
bleu: str
vert: str
rouge: str
blanc: str
cyan: str
reset: str

jaune = "\033[33m"
gris = "\033[90m"
magenta = "\033[35m"
bleu = "\033[34m"
vert = "\033[32m"
rouge = "\033[31m"
blanc = "\033[37m"
cyan = "\033[36m"
rose = "\033[95m"

reset = "\033[0m"
