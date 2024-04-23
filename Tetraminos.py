"""
Auteur : Dias Valentin

date : 14/12/23

but : Le jeu des tetraminos est un jeu hors ligne qui consiste à emboiter des formes géométriques simples
    dans un rectangle central jusqu'à le recouvrir entièrement. Ce jeu te propose 3 niveaux de difficultés (1, 2 ou 3).
    Tu disposes d'autant de temps que tu le souhaites pour remporter la partie. Un compteur enregistre le nombre de
    mouvements effectués te permettant ainsi de t'améliorer de partie en partie.
    ATTENTION: Pour gagner, il faut impérativement que le carré central soit entièrement complété et qu'aucun
    tetraminos ne se chevauchent ou ne soient posés sur une des limites de la zone de jeu.
Entrées : un espace pour commencer le jeu et ensuite un numéro pour chosir un tetramino(1-8) suivi de i pour aller
vers le haut, k en bas, j à gauche, l à droite, u rotation anti-horaire, o pour une rotation horaire et pour finir v
pour poser le tetramino choisi

Sorties : Une grille avec des tetraminos qui se déplacent en fonction de l'input de l'utilisateur ainsi qu'un affichage
        de presentation du jeu et de sa victoire en cas de victoire
"""

import sys
from getkey import getkey
import os


# f string, double return quoi mettre en arguments, erreur global, press start pour commencer


def print_rules():
    """
    Fonction servant à print les règles du jeu au lancement de celui-ci.
    :return: /
    """
    for space in range(5):
        print()
    print(" Règles du jeu :")
    print()
    print(" Le jeu des tetraminos est un jeu hors ligne qui consiste à emboiter des formes géométriques simples"
          " dans un rectangle central jusqu'à le recouvrir"), print(" entièrement. Ce jeu te propose 3 niveaux "
                                                                    "de difficultés (1, 2 ou 3). Tu disposes d'autant "
                                                                    "de temps que tu le souhaites pour remporter la "
                                                                    "partie. "),
    (print(" Un compteur enregistre le nombre de mouvements effectués te permettant ainsi"
           " de t'améliorer de partie en partie."), print("ATTENTION: Pour gagner, il faut impérativement que le "
                                                          "rectangle central soit entièrement complété et que les "
                                                          "tetraminos ne se chevauchent pas"),
     print(" ou ne soient posés sur une des limites de la zone de jeu."))
    for space in range(5):
        print()
    print(" " * 45, end=''), print("\033[0;1m\033[92m""Appuie sur la barre d'espace pour commencer le jeu""\033[97m")


def print_starting_game():
    """
    Fonction servant à print le titre du jeu grâce à de l'art ascii (trouvé sur internet).
    :return: /
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # permet de clear le terminal avant d'afficher le titre du jeu
    print("\033[92m"
          r"""
         ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
         ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
             ▐░▌     ▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌▐░▌          
             ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
             ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
             ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
             ▐░▌     ▐░▌               ▐░▌     ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌          ▐░▌
             ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░▌      ▐░▌ ▐░▌       ▐░▌▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
             ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
              ▀       ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀         ▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                                                                                                                                                                        
                                                                                                                            BY Valentin DIAS, 2023
""""\033[97m")


def keybinds(tetramino: list):
    """
    Fonction servant à print les touches du clavier permettant de jouer au jeu.
    :param tetramino:
    :return: /
    """
    size = len(tetramino)  # recupération du nombre de tetraminos sur le plateau de jeu
    for line in range(3):
        print()
    print("touches:"), print(), print(" " * 11, "prendre un tetramino : ", end=''),
    print(" " * 16, "déplacement :", end=''),
    print(" " * 25, "rotation :", end=''), print(" " * 23, "poser un tetramino :")
    print()
    print(" " * 7, f"(\033[1;34m1 - {size}\033[97m) : prendre le tetramino", end=''),  # le fstring avec size pour que
    # l'affichage des touches pour selectionner un tetramino change en fonction du nombre de tetraminos sur le plateau
    print(" " * 3, "(\033[1;34mi\033[97m) : le déplacer vers le haut", end=''),
    print(" " * 5, "(\033[1;34mo\033[97m) : le tourner dans le sens horaire", end=''),
    print(" " * 6, "(\033[1;34mv\033[97m) : poser le tetramino")
    print()
    print(" " * 41, "(\033[1;34mk\033[97m) : le déplacer vers le bas", end=''),
    print(" " * 6, "(\033[1;34mu\033[97m) : le tourner dans le sens anti-horaire")
    print()
    print(" " * 41, "(\033[1;34ml\033[97m) : le déplacer vers la droite")
    print()
    print(" " * 41, "(\033[1;34mj\033[97m) : le déplacer vers la gauche")


def scoreboard(number):
    """
    Fonction pour placer le tableau des score et mettre en couleur le nombre qu'y s'y trouve.
    :param number: le nombre de mouvements de l'utilisateur.
    :return: /
    """
    for space in range(100):  # faire des print pour placer le scoreboard du coté gauche
        print(' ', end='')
    for bottom_dash in range(4):  # print les tirets du bas
        print("__", end='')
    print()
    for espace in range(100):  # print les espaces et apres les barres
        print(' ', end='')
    print("|      |")
    if number >= 0:  # condition toujours satisfaite et après placera les numeros en couleurs du bleu au rouge.
        for espace in range(77):
            print(' ', end='')
        print("Nombre de mouvements : ", end='')
        if number >= 0 and number <= 9:
            print(f"|  \033[0;94m{number}\033[97m   |")
        if number >= 10 and number <= 99:
            print(f"|  \033[0;92m{number}\033[97m  |")
        if number >= 100 and number <= 999:
            print(f"|  \033[93m{number}\033[97m |")
        if number >= 1000 and number <= 9999:
            print(f"| \033[0;91{number}\033[97m |")
    for espace in range(100):
        print(' ', end='')
    print("|      |")
    for espace in range(100):
        print(' ', end='')
    for top_dash in range(4):
        print("‾‾", end='')
    print()
    return number


def import_card(fill_path: str) -> tuple:
    """
    Cette fonction va ouvrir le fichier de la carte afin de recupérer la taille du plateau a
    :param fill_path: string de carte que le joueur souhaite utiliser pour son jeu
    :return: un tuple contenant un tuple (x, y) avec x et y la longueur et la largeur du plateau de jeu,
    ainsi que les coordonnées des tetraminos sous forme deliste
    """
    with open(fill_path, "r") as f:
        count_all = len(f.readlines())  # ouverture du fichier txt pour recéperer le nombre de lignes de ceelui-ci
    with open(fill_path, "r") as f:
        line_counter = 0
        tetramino_lst = []
        color_list = []
        for line in f.readlines():
            if line_counter == 0:
                sx, sy = line.split(",")  # split le x et le y avce la virgule
                x, y = int(sx), int(sy)  # transformer le x et y qui sont des strings en int
                tuple = (x, y)
                line_counter += 1
            else:
                if line_counter == count_all:
                    color_list.append(line[-7:])
                    point_replace = line[:-9].replace(";", ", ")
                else:  # le else est là parce que pour chaque couleur la couleur finie par un espace(\n) sauf la
                    # dernière ligne
                    point_replace = line[:-10].replace(";", ", ")
                    color_list.append(line[-8: - 1])
                tetramino_lst.append(point_replace)
                color_list.append((0, 0))
            line_counter += 1
        not_str = []
        for i in tetramino_lst:
            str_count = 0
            str_temporate = []
            lenght = (len(i) - 6) // 8  # le - 6 parce que le premier element de la liste de tetramino aura toujours une
            # taille de 6 et le // par 8 parce que pour tous les autres elements la taille est de 8
            benchmark = 1
            while str_count <= lenght:
                str_temporate.append(
                    (int(i[benchmark]), int(i[benchmark + 3])))  # liste temporaire pour récupérer chaque
                # x et y de chaque tuple et pour chaque tetramino et ainsi de les stocker dans une liste qui se
                # reinitialise à chaque tetraminos.
                str_count += 1
                benchmark += 8  # car les tuples ont 8 caractères d'espace entre eux.
            not_str.append(str_temporate)
        count_color = 0
        count = 0
        tetramino = []
        for element in tetramino_lst:
            tetramino.append([not_str[count], color_list[count_color], (0, 0)])
            count_color += 2  # ee saut pour les couleurs est de 2, car la liste couleur est composé d'un code couleur
            # suivi
            # du decalage (0,0) mais onne veut que le code couleur donc on saute à chaque fois le tuple (0,0)
            count += 1  # pour recuperer chaque tetraminos 1 par 1 dans la liste des tetraminos
    return (tuple, tetramino)


def create_grid(w: int, h: int) -> list:
    """
    Fonction pour créer la grille qui est une matrice à l'aide du H et W recu par la fonction import_card
    :param w: le nombre de colonnes de la matrice donc les x
    :param h: le nombre de lignes de la matrice donc lex y
    :return: la grid qui est une liste, ici une matrice de taille (3w + 2) X (3h + 2)
    """
    grid = [["  " for columns in range(3 * w + 2)] for rows in range(3 * h + 2)]
    for i in range(w):  # avec ce for, on parcourt les lignes de la matrice
        grid[h][w + 1 + i] = '--'
        grid[h + 1 + h][w + 1 + i] = '--'
        for j in range(h):  # avec ce fort imbriqué, on parcourt les colonnes de la matrice
            grid[h + 1 + j][w] = " |"
            grid[h + 1 + j][w + 1 + w] = "| "
    return grid


def setup_tetraminos(tetraminos: list, grid: list):
    """
    La fonction ne sera appelé qu'une fois au debut du jeu afin de placer les tetraminos dans la grille et dans leur
    "sous-matrice" (sans ça les tetraminos serait tous dans le coin suppérieur gauche) en modifiant le décalage
    :param tetraminos: liste de tetraminos avec un decalage de (0,0)
    :param grid: une matrice vierge
    :return: la grille (qui est une liste) avec les tetraminos placés et la liste des tetraminos avce le décalage modifié.
    """
    offset_x, offset_y, column_size = int(), int(), int()  # sert à les définir

    tetraminos_list = []
    color_list = []
    decalage_list = []
    for coor_tuple in tetraminos:
        tetraminos_list.append(coor_tuple[0])
        color_list.append(coor_tuple[1])
        decalage_list.append(coor_tuple[2])
    for line in grid:
        column_size = (len(line)) // 3 + 1  # on veut que la liste soit séparée en 9 zones (3X3) avec la zone
        # centrale vide,
        # on doit donc diviser les colonnes par 3 et placer le premier tatramino dans la première et le + 1, car on
        # veut des sous-matrices de meme taille donc la suivante doit commencer 1 plus loin pour ne pas se supperposé
        # avec celle se trouvant à côté
    line_size = len(grid) // 3 + 1  # on veut que la liste soit séparée en 9 zones (3X3) avec la zone centrale vide
    # on doit donc divser les lignes par 3 et placer le premier tatramino dans la première et le + 1, car on veut
    # des sous-matrices de meme taille donc la suivante doit commencer 1 plus bas pour ne pas se supperposer avec celle
    # se trouvant en dessous
    x, y = 0, 0
    coor_decalge = [(x, y), (x + column_size, y), (x + 2 * column_size, y), (x, y + line_size),
                    (x + 2 * column_size, y + line_size), (x, y + 2 * line_size), (x + column_size, y + 2 * line_size),
                    (x + 2 * column_size,
                     y + 2 * line_size)]  # liste avec tous les decalages pour les 8 tetraminos sachant
    # la zone centrale n'est pas dedans car aucun tetramino ne doit s'y trouver dedans
    tetramino = []
    color_turn = 1
    for i in range(len(tetraminos_list)):
        tetramino.append([tetraminos_list[i], color_list[i], (0, 0)])
        color_turn += 1
    grid_turn = 0
    for lst_coordonates in range(len(tetraminos)):
        for xy_coordonates in range(len(tetraminos[grid_turn][0])):
            xy = tetraminos[grid_turn][0][xy_coordonates]
            x = int(xy[0])
            y = int(xy[1])
            offset_x = int(coor_decalge[lst_coordonates][0])
            offset_y = int(coor_decalge[lst_coordonates][1])
            grid[y + offset_y][x + offset_x] = f'\x1b[{tetraminos[grid_turn][1]}m{grid_turn + 1} \x1b[0m'  # addition
            # des coordonnées des tetraminos avec leur decalage pour les placer dans la grille
        tetramino[lst_coordonates][2] = (offset_x, offset_y)
        grid_turn += 1
    return grid, tetramino


def place_tetraminos(tetraminos: list, grid: list) -> list:
    """
    Fonction qui recrée une nouvelle grille vierge pour y placer les tetraminos recu en argument de la fonction
    :param tetraminos: liste des tetraminos (coordonnées, couleurs et le décalage)
    :param grid: liste qui représente la grille (sous forme de matrice)
    :return:la grid avec les tetraminos qui sont posés dedans
    """
    w = int()  # sers juste à définir h
    for i in range(len(grid)):
        for j in range(len(grid)):
            w = (len(
                grid[0]) - 2) // 3  # à partir de la grille de base en faisant le calcul inverse, on sait retrouver le w
    h = (len(grid) - 2) // 3  # à partir de la grille de base en faisant le calcul inverse, on sait retrouver le h
    grid = create_grid(w, h)
    grid_turn = 0
    coordinates_lst_xy = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '  ':
                coordinates_lst_xy.append((j, i))
    for lst_coordonates in range(len(tetraminos)):
        for xy_coordonates in range(len(tetraminos[grid_turn][0])):
            xy = tetraminos[grid_turn][0][xy_coordonates]
            x = int(xy[0])
            y = int(xy[1])
            offset_x = int(tetraminos[grid_turn][2][0])
            offset_y = int(tetraminos[grid_turn][2][1])
            tuple_xy = (x + offset_x, y + offset_y)
            if tuple_xy not in coordinates_lst_xy:
                coordinates_lst_xy.append((x + offset_x, y + offset_y))
                grid[y + offset_y][x + offset_x] = f'\x1b[{tetraminos[grid_turn][1]}m{grid_turn + 1} \x1b[0m'
            else:
                grid[y + offset_y][x + offset_x] = f'\x1b[{tetraminos[grid_turn][1]}mXX\x1b[0m'  # place XX si le
                # tetramino chevauche un autre ou se trouve au-dessus d'un bord du plateau
        grid_turn += 1
    return grid


def rotate_tetramino(tetramino: list, clockwise: bool = True) -> list:
    """
    Fonction permettant d'effectuer la rotation d'un tetramino
    :param tetramino: le tetramino que l'on souhaite tourner
    :param clockwise: le sens dans lequel on veut tourner le tetramino
    :return: la liste du tetramino avce ses coordonnées modifiées en fonction du sens de rotation choisis
    """
    tuple_xy = []
    color = tetramino[1:]
    for coor_tuple in tetramino[0]:
        x = int(coor_tuple[0])
        copy_of_x = int(coor_tuple[0])  # copie du x pour pouvoir modifier la valeur de x qui subira la rotation  tout en
        # gardant la valeur initiale du x
        y = int(coor_tuple[1])
        if clockwise:
            x = -y
            y = copy_of_x
        if not clockwise:
            x = y
            y = -copy_of_x
        tuple_xy.append((x, y))
    tetramino = [tuple_xy, *color]
    return tetramino


def check_move(tetramino: list, grid: list) -> bool:
    """
    Fonction qui vérifie les cellules de la matrice et s'assure qu'aucun XX n'est present (signe qu'un tetramino
    n'est pas au bon endroit)
    :param tetramino: Pas utilisé dans ma fonction
    :param grid: grille avec les tetraminos
    posées dedans
    :return:un booleen qui indique True si tous les tetraminos sont bien placés et False si un
    tetraminos est situé à un endroit où il ne devrait pas
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for color in range(10):  # j'ai remarqué que les codes couleurs utilisés sont toujours compris entre 40 et
                # 49 ma fonction va donc voir pour chaque cellule de la matrice si le code couleur suivi de XX est
                # present et donc pour chaque cellule il va tester les 10 combinaisons de couleurs.
                if grid[i][j] == f'\x1b[0;37;4{color}mXX\x1b[0m':
                    return False
    return True


def choice_tetramino(num, teraminos) -> list:
    """
    :param num: un string du numéro entré en input par l'utilisateur
    :param teraminos: la liste des tetraminos
    :return: un tetramino qui est celui que l'utilisateur a choisi
    """
    num = int(num)  # le numéro entré par l'utilisateur est un chiffre sous forme de string et pas un int()
    color = []
    tetramino_coor = []
    color.append(teraminos[num][1:])
    for i in range(len(teraminos[num][0])):
        tetramino_coor.append(teraminos[num][0][i])
    return [tetramino_coor, *color]


def move(tetramino, key) -> list:
    """
    Fonction qui modifie les x et/ou y du decalage des tetraminos pour effectuer des mouvements verticaux et
    horizontaux
    :param tetramino:
    :param key: la lettre entrée par l'utilisateur
    :return: le tetramino avec son décalage modifié
    """
    decalage = tuple  # pour definir le décalage
    if key == 'i':
        decalage = (int(tetramino[1][1][0]), int(tetramino[1][1][1]) - 1)
    if key == 'k':
        decalage = (int(tetramino[1][1][0]), int(tetramino[1][1][1]) + 1)
    if key == 'j':
        decalage = int(tetramino[1][1][0]) - 1, int(tetramino[1][1][1])
    if key == 'l':
        decalage = int(tetramino[1][1][0]) + 1, int(tetramino[1][1][1])
    tetramino[1][1] = decalage
    return tetramino


def print_grid(grid: list, no_number: bool, number_of_mouvements) -> list:
    """
    Fonction servant simplement à print la grille
    :param grid:
    :param no_number: booleen qui indique si les nombres doivent apparaitre sur les tetraminos ou pas
    :param number_of_mouvements: le score du joueur donc son nombre de mouvements
    :return: la grille qui est une matrice vierge
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(2):
        print()
    scoreboard(number_of_mouvements)  # appel à la fonction qui print le tableau des scores
    print(" " * 58, end="")
    print('__' * len(grid[0]), end='')
    print('__')
    if not no_number:
        for i in range(len(grid)):
            print(" " * 58, end="")
            print('|', end='')
            for j in range(len(grid[i])):
                print(grid[i][j], end='')
            print('|', end='')
            print()
    else:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                for color in range(10):
                    for number in range(10):
                        if grid[i][j] == f'\x1b[0;37;4{color}m{number} \x1b[0m':
                            grid[i][j] = f'\x1b[0;37;4{color}m  \x1b[0m'
                        if grid[i][j] == f'\x1b[1;37;40m{number} \x1b[0m':  # vérifie la couleur noire et remplace par
                            # * pour voir le tetramino noir meme sur fond noir
                            grid[i][j] = f'\x1b[1;37;40m* \x1b[0m'
                        if grid[i][j] == f'\x1b[0;30;47m{number} \x1b[0m':  # vérifie la couleur blanche et remplace
                            # par * pour voir le tetramino blanc meme sur fond blanc
                            grid[i][j] = f'\x1b[1;37;40m* \x1b[0m'

        for i in range(len(grid)):
            print(" " * 58, end="")
            print('|', end='')
            for j in range(len(grid[i])):
                print(grid[i][j], end='')
            print('|', end='')
            print()
    print(" " * 58, end="")
    print('‾‾' * len(grid[0]), end='')
    print('‾‾')
    return grid


def limits(tetramino, mouvement, grid) -> bool:
    """
    Fonction pour définir les limites de la grille pour empecher les tetraminos d'avoir des coordonnées negatives et
    donc sortir de la grille
    :param tetramino:les coordonnées d'un tetramino
    :param mouvement: le mouvement que l'utilisateur veut effectuer
    :param grid:la grille pour connaitre sa taille et donc ses limites
    :return: un booleen qui dit si la position du tetraminos est hors limites ou non
    """
    for coor_tuple in mouvement:
        x = int(coor_tuple[0])
        y = int(coor_tuple[1])
        decx = tetramino[1][1][0]
        decy = tetramino[1][1][1]
        if x + decx < 0 or y + decy < 0:
            return False
        if y + decy > len(grid) - 1:  # le - 1 car la len de la grille est 1 plus grand que la taille en indice de la
            # grille car les indices commencent par 0
            return False
        for i in grid:
            for j in grid:
                if x + decx > len(j) - 1:  # le - 1 car la len de la grille est 1 plus grand que la taille en indice de
                    # la grille car les indices commencent par 0
                    return False
    return True


def check_win(grid: list) -> bool:
    """
    Fonction pour vérifier si l'utilisateur à gagner ou non donc si le carré central est bien complet
    :param grid: afin de checker son carré central
    :return:un booleen qui indique si le joueur à gagner ou pas encore
    """
    w = int()  # sers à le définir
    numbers = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            w = (len(grid[0]) - 2) // 3
    h = (len(grid) - 2) // 3
    for i in range(w):
        for j in range(h):
            if grid[h + 1 + j][w + 1 + i] != '  ':
                numbers += 1
    if numbers == w * h:
        return True
    return False


def print_win(number_of_mouvements):
    """
    Fonction qui print un art ascii en cas de victoire
    :param number_of_mouvements: le nombre de movements effectués
    :return: /
    """
    print(f"\033[92mTu as terminé le jeu en {number_of_mouvements} mouvements")
    print(r"""             ____   ____    ____  __ __   ___                                              
            |    \ |    \  /    ||  |  | /   \                                             
            |  o  )|  D  )|  o  ||  |  ||     |                                            
            |     ||    / |     ||  |  ||  O  |                                            
            |  O  ||    \ |  _  ||  :  ||     | __                                         
            |     ||  .  \|  |  | \   / |     ||  |                                        
            |_____||__|\_||__|__|  \_/   \___/ |__|                                        
                                                \|                                        
                    ______  __ __       ____  _____      ____   ____   ____  ____     ___      __ 
                   |      ||  |  |     /    |/ ___/     /    | /    | /    ||    \   /  _]    |  |
                   |      ||  |  |    |  o  (   \_     |   __||  o  ||   __||  _  | /  [_     |  |
                   |_|  |_||  |  |    |     |\__  |    |  |  ||     ||  |  ||  |  ||    _]    |__|
                     |  |  |  :  |    |  _  |/  \ |    |  |_ ||  _  ||  |_ ||  |  ||   [_      __ 
                     |  |  |     |    |  |  |\    |    |     ||  |  ||     ||  |  ||     |    |  |
                     |__|   \__,_|    |__|__| \___|    |___,_||__|__||___,_||__|__||_____|    |__|
                                                                                       """"\033[97m")


def main():
    win = False
    print_starting_game()
    print_rules()
    key = getkey().decode('utf-8')
    if key == ' ':
        count_moves = 0
        file_path = sys.argv[1]
        reading_tetra = import_card(file_path)
        matrix = create_grid(reading_tetra[0][0], reading_tetra[0][1])
        tetraminos_position = setup_tetraminos(reading_tetra[1], matrix)
        tetraminos_placed = place_tetraminos(tetraminos_position[1], matrix)
        print_grid(matrix, no_number=False, number_of_mouvements=count_moves)
        keybinds(tetraminos_position[1])
        while not win:
            key = getkey().decode('utf-8')
            if key.isdecimal():
                while int(key) > len(tetraminos_position[1]) or int(key) == 0:
                    print(), print(f"Veuillez entrer le numéro d'un tetramino entre 1 et {len(tetraminos_position[1])}")
                    key = getkey().decode('utf-8')
                key = int(key) - 1
                print_grid(tetraminos_placed, no_number=True, number_of_mouvements=count_moves)
                keybinds(tetraminos_position[1])
                key2 = '-'
                while key2 != 'v':
                    choice = choice_tetramino(key, tetraminos_position[1])
                    key2 = getkey().decode('utf-8')
                    key2 = key2.lower()
                    if key2 == 'o':
                        rotation = rotate_tetramino(choice, True)
                        lim = limits(choice, rotation[0], matrix)
                        if lim:
                            tetraminos_position[1][int(key)][0] = rotation[0]
                            count_moves += 1
                        tetraminos_placed = place_tetraminos(tetraminos_position[1], matrix)
                        print_grid(tetraminos_placed, no_number=True, number_of_mouvements=count_moves)
                        keybinds(tetraminos_position[1])
                        if not lim:
                            print(), print(
                                f"La rotation vers la gauche ne peut pas etre effectuée car le tetramino {int(key) + 1} "
                                f"est trop proche du bord")
                    if key2 == 'u':
                        rotation = rotate_tetramino(choice, False)
                        lim = limits(choice, rotation[0], matrix)
                        if lim:
                            tetraminos_position[1][int(key)][0] = rotation[0]
                            count_moves += 1
                        tetraminos_placed = place_tetraminos(tetraminos_position[1], matrix)
                        print_grid(tetraminos_placed, no_number=True, number_of_mouvements=count_moves)
                        keybinds(tetraminos_position[1])
                        if not lim:
                            print(), print(
                                f"La rotation vers la droite ne peut pas etre effectuée car le tetramino {int(key) + 1}"
                                f"est trop proche du bord")
                    if key2 == 'i' or key2 == 'k' or key2 == 'j' or key2 == 'l':
                        your_move = move(choice, key2)
                        lim = limits(choice, your_move[0], matrix)
                        if lim:
                            tetraminos_position[1][int(key)][2] = your_move[1][1]
                            count_moves += 1
                        tetraminos_placed = place_tetraminos(tetraminos_position[1], matrix)
                        print_grid(tetraminos_placed, no_number=True, number_of_mouvements=count_moves)
                        keybinds(tetraminos_position[1])
                        if not lim:
                            print(), print(f'Le tetramino {int(key) + 1} ne pas pas etre déplacé en dehors du plateau')
                    if key2 == 'v':
                        matrix = tetraminos_placed
                        checking_move = check_move(tetraminos_position[1][int(key)], matrix)
                        if checking_move:
                            tetraminos_placed = place_tetraminos(tetraminos_position[1], matrix)
                        visual_grid = print_grid(tetraminos_placed, no_number=False, number_of_mouvements=count_moves)
                        keybinds(tetraminos_position[1])
                        if not checking_move:
                            print(), print(f"Le tetramino {int(key) + 1} est posé sur un bord ou un autre tetramino, "
                                           "Veuillez le déplacer")
                            key2 = key
                        win = check_win(visual_grid)
    if win:
        print_grid(tetraminos_placed, no_number=True, number_of_mouvements=count_moves)  # dis que tatraminos_placed et
        # count_move ne sont pas définis, mais ils le sont
        print_win(number_of_mouvements=count_moves)
        return True


if __name__ == '__main__':
    main()
