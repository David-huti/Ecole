def afficher_plateau(plateau):
# Afficher chaque ligne du plateau
     for ligne in plateau:
         print(" | ".join(ligne))
         print("---------")


def verifier_victoire(plateau, signe):
# Vérifier les lignes horizontales
    for ligne in plateau:
        if ligne[0] == signe and ligne[1] == signe and ligne[2] == signe:
          return True

# Vérifier les colonnes verticales
    for colonne in range(3):
        if plateau[0][colonne] == signe and plateau[1][colonne] == signe and plateau[2][colonne] == signe:
         return True

# Vérifier les diagonales
    if plateau[0][0] == signe and plateau[1][1] == signe and plateau[2][2] == signe:
       return True

    if plateau[0][2] == signe and plateau[1][1] == signe and plateau[2][0] == signe:
     return True

    return False


def jouer():
# Créer un plateau vide
    plateau = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    signe = "X"
    tours = 0

# Continuer tant que la partie n'est pas terminée
    while tours < 9:
         afficher_plateau(plateau)
        
         print("Au tour du joueur", signe)

         ligne = int(input("Choisis une ligne (1, 2 ou 3) : ")) - 1
         colonne = int(input("Choisis une colonne (1, 2 ou 3) : ")) - 1
        
         print("Entre un nombre valide.")
    else:

# Vérifier que les coordonnées sont valides
     if ligne not in range(3) or colonne not in range(3):
        print("Choisis une ligne et une colonne entre 1 et 3.")
     else:

# Vérifier que la case est libre
      if plateau[ligne][colonne] != " ":
         print("Cette case est déjà occupée.")
      else:

# Placer le signe du joueur
       plateau[ligne][colonne] = signe
    tours += 1

# Vérifier si le joueur a gagné
    if verifier_victoire(plateau, signe):
        afficher_plateau(plateau)
        print("Le joueur", signe, "a gagné !")
        return
# Changer de joueur
    if signe == "X":
       signe = "O"
    else:
        signe = "X"

# Si les neuf cases sont remplies sans victoire
    afficher_plateau(plateau)
    print("Match nul !")


# Lancer le jeu
jouer()