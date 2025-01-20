# Projet Python : Mini-Jeux Interactifs

Ce projet a été réalisé dans le cadre de la SAE 1.01. Il propose un ensemble de mini-jeux interactifs jouables en mode console, mettant en œuvre des fonctionnalités telles que la gestion des joueurs et la sauvegarde des scores.

---

## **Description**
Ce programme offre une expérience ludique pour deux joueurs grâce à un menu interactif permettant de naviguer entre les différentes sections :

- **Gestion des joueurs** :
  - Création de nouveaux joueurs.
  - Sélection et suppression de joueurs.
- **Mini-jeux disponibles** :
  - Jeu des Allumettes : Retirez 1, 2 ou 3 allumettes. Le joueur qui retire la dernière allumette perd.
  - Devinette : Trouvez un nombre secret dans une plage définie avec un nombre d'essais limité.
  - Morpion : Alignez trois symboles sur une grille 3x3 pour gagner.
  - Puissance 4 : Alignez quatre jetons sur une grille 6x7.
- **Gestion des scores** :
  - Affichage des classements.
  - Sauvegarde et chargement des scores.
  - Réinitialisation des données.

---

## **Structure du projet**
Le projet est organisé selon une architecture modulaire :

```
projet/
|-- main.py                        # Point d'entrée du programme
|-- base/
|   |-- interface_joueurs.py       # Gestion des joueurs
|   |-- sauvegarde.py              # Sauvegarde des données
|   |-- menuJoueurs.py             # Menu de gestion des joueurs
|   |-- menuScoreSave.py           # Gestion des scores
|   |-- outils.py                  # Fonctions utilitaires
|-- jeux/
|   |-- menuJeux.py                # Menu de sélection des jeux
|   |-- allumette/
|   |   |-- __init__.py            # Initialisation du module allumette
|   |   |-- bot_allumette.py       # IA pour le jeu des allumettes
|   |   |-- jeu_allumette.py       # Logique du jeu des allumettes
|   |   |-- joueur_allumette.py    # Gestion des joueurs pour le jeu des allumettes
|   |-- devinette/
|   |   |-- __init__.py            # Initialisation du module devinette
|   |   |-- bot_devinette.py       # IA pour le jeu de devinette
|   |   |-- jeu_devinette.py       # Logique du jeu de devinette
|   |   |-- joueur_devinette.py    # Gestion des joueurs pour le jeu de devinette
|   |-- morpion/
|   |   |-- __init__.py            # Initialisation du module morpion
|   |   |-- bot_morpion.py         # IA pour le jeu de morpion
|   |   |-- jeu_morpion.py         # Logique du jeu de morpion
|   |   |-- joueur_morpion.py      # Gestion des joueurs pour le jeu de morpion
|   |-- puissance4/
|       |-- __init__.py            # Initialisation du module puissance 4
|       |-- bot_puissance4.py      # IA pour le jeu de puissance 4
|       |-- jeu_puissance4.py      # Logique du jeu de puissance 4
|       |-- joueur_puissance4.py   # Gestion des joueurs pour le jeu de puissance 4
```

---

## **Prérequis**
- Python
- Aucun module externe requis (les bibliothèques standards sont utilisées).

---

## **Installation et exécution**
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Bessastien/Mini-jeux-Interactifs.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd projet
   ```
3. Lancez le programme :
   ```bash
   python main.py
   ```

---

## **Utilisation**
Le programme s'exécute entièrement en console. Naviguez dans les menus en entrant les numéros correspondant aux options souhaitées.

- **Menu principal** : Permet d'accéder aux différentes sections du programme.
- **Menu Joueurs** : Gérez les profils des joueurs.
- **Menu Jeux** : Choisissez et jouez à l'un des quatre mini-jeux.

---

## **Tests et validation**
Des jeux d’essais ont été réalisés pour valider les fonctionnalités principales :

- Gestion correcte des entrées utilisateurs (valeurs valides et invalides).
- Sauvegarde et chargement des données via le module `pickle`.
- Détection des conditions de victoire ou d’échec dans chaque jeu.

---

## **Améliorations futures**
Voici quelques idées pour enrichir ce projet :

- Projet fini

---

## **Contributeurs**
- **Sébastien Dabert** - Étudiant BUT 1 INFO, Groupe 3b.
- **Célia Larousse** - Étudiante BUT 1 INFO, Groupe 3b.