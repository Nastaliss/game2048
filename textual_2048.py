def read_player_command():
    move= ""
    while not move in ["g","d","h","b"]:
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move

def read_size_grid():
    size=""
    while not size.isdigit():
        size = input("Entrez la taille de la grille")
    return size

def read_theme_grid():
    theme=""
    while not theme in ["0","1","2"]:
        theme = input ("Entrez le numero du theme")
    return theme

