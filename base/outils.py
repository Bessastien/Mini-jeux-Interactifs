from os import system, name
from time import sleep


def clear() -> None:
    """
    Cette fonction permet de nettoyer la console.

    Elle détecte le système d'exploitation et exécute la commande appropriée pour nettoyer la console.

    Returns:
        None
    """
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Linux
    else:
        _ = system('clear')
    print()


def attendre() -> None:
    """
    Cette fonction permet de faire une pause dans l'exécution du programme.

    Elle utilise la fonction sleep pour suspendre l'exécution pendant 1,2 seconde.

    Returns:
        None
    """
    sleep(1.2)


def passer() -> None:
    """
    Cette fonction permet de faire une pause dans l'exécution du programme jusqu'à ce que l'utilisateur appuie sur la touche Entrée.

    Returns:
        None
    """
    input("Appuyez sur la touche 'Entrée' pour continuer...")


# OUTILS DE COULEURS
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
orange = "\033[91m"
reset = "\033[0m"

