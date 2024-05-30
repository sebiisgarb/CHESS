import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
BOARD_SIZE = 8
SQUARE_SIZE = SCREEN_WIDTH // BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BROWN = (139, 69, 19)
LIGHT_BROWN = (222, 184, 135)

timer = pygame.time.Clock()
fps = 60

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess")

# game variables and images

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                  (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
captured_pieces_white = []

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                  (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_black = []

# 0 - whites turn no selection : 1-whites turn, piece selected: 2 black turn no selection : 3 black turn selection
turn_step = 0
selection = 100
valid_moves = []

# Load and scale black queen
black_queen = pygame.image.load('Pieces/black-queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (20, 20))

# Load and scale white queen
white_queen = pygame.image.load('Pieces/white-queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (20, 20))

# Load and scale black king
black_king = pygame.image.load('Pieces/black-king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (20, 20))

# Load and scale white king
white_king = pygame.image.load('Pieces/white-king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (20, 20))

# Load and scale black rook
black_rook = pygame.image.load('Pieces/black-rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (20, 20))

# Load and scale white rook
white_rook = pygame.image.load('Pieces/white-rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (20, 20))

# Load and scale black bishop
black_bishop = pygame.image.load('Pieces/black-bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (20, 20))

# Load and scale white bishop
white_bishop = pygame.image.load('Pieces/white-bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (20, 20))

# Load and scale black knight
black_knight = pygame.image.load('Pieces/black-knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (20, 20))

# Load and scale white knight
white_knight = pygame.image.load('Pieces/white-knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (20, 20))

# Load and scale black pawn
black_pawn = pygame.image.load('Pieces/black-pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (80, 80))
black_pawn_small = pygame.transform.scale(black_pawn, (20, 20))

# Load and scale white pawn
white_pawn = pygame.image.load('Pieces/white-pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (80, 80))
white_pawn_small = pygame.transform.scale(white_pawn, (20, 20))

white_images = [white_pawn, white_knight, white_rook, white_bishop, white_queen, white_king]
black_images = [black_pawn, black_knight, black_rook, black_bishop, black_queen, black_king]
small_white_images = [white_pawn_small, white_knight_small, white_rook_small, white_bishop_small, white_queen_small,
                      white_king_small]
small_black_images = [black_pawn_small, black_knight_small, black_rook_small, black_bishop_small, black_queen_small,
                      black_king_small]

piece_list = ['pawn', 'knight', 'rook', 'bishop', 'queen', 'king']


# check variables


def draw_board():
    colors = [LIGHT_BROWN, DARK_BROWN]
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


current_turn = "white"


def change_turn():
    global current_turn
    current_turn = "black" if current_turn == "white" else "white"


board = [[None for _ in range(8)] for _ in range(8)]


# draw pieces onto board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index((white_pieces[i]))
        screen.blit(white_images[index], (white_location[i][0] * 100 + 10, white_location[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red',
                                 [white_location[i][0] * 100 + 1, white_location[i][1] * 100 + 1, 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index((black_pieces[i]))
        screen.blit(black_images[index], (black_location[i][0] * 100 + 10, black_location[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue',
                                 [black_location[i][0] * 100 + 1, black_location[i][1] * 100 + 1, 100, 100], 2)


# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_location and (position[0], position[1] + 1) not in black_location and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_location and (position[0], position[1] + 2) not in black_location and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_location:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_location:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in black_location and (position[0], position[1] - 1) not in white_location and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in black_location and (position[0], position[1] - 2) not in white_location and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_location:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_location:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

def check_queen(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        enemies_list = white_location
        friends_list = black_location

    for i in range(4):  # checking down up right left
        path = True
        path2 = True
        chain = 1
        chain2 = 1
        if i == 0:
            x = 0
            y = 1
            z = 1
            q = 1
        elif i == 1:
            x = 0
            y = -1
            z = -1
            q = 1
        elif i == 2:
            x = 1
            y = 0
            z = 1
            q = -1
        elif i == 3:
            x = -1
            y = 0
            z = -1
            q = -1

        while path:
            if (position[0] + chain * x, position[1] + chain * y) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + chain * x, position[1] + chain * y) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
        while path2:
            if (position[0] + chain2 * z, position[1] + chain2 * q) not in friends_list and 0 <= position[0] + chain2 * z <= 7 and 0 <= position[1] + chain2 * q <= 7:
                moves_list.append((position[0] + chain2 * z, position[1] + chain2 * q))
                if (position[0] + chain2 * z, position[1] + chain2 * q) in enemies_list:
                    path2 = False
                chain2 += 1
            else:
                path2 = False
    return moves_list


def check_king(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_location
    else:
        friends_list = black_location
    for i in range(4):
        if i == 0:
            x = 0
            y = 1
            z = 1
            q = 1
        elif i == 1:
            x = 0
            y = -1
            z = -1
            q = 1
        elif i == 2:
            x = 1
            y = 0
            z = 1
            q = -1
        elif i == 3:
            x = -1
            y = 0
            z = -1
            q = -1
        if (position[0] + x, position[1] + y) not in friends_list and 0 <= position[0] + x <= 7 and 0 <= position[1] + y <= 7:
            moves_list.append((position[0] + x, position[1] + y))
        if (position[0] + z, position[1] + q) not in friends_list and 0 <= position[0] + z <= 7 and 0 <= position[1] + q <= 7:
            moves_list.append((position[0] + z, position[1] + q))
    return moves_list



def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        enemies_list = white_location
        friends_list = black_location

    for i in range(4):  # checking down up right left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        elif i == 3:
            x = -1
            y = 0

        while path:
            if (position[0] + chain * x, position[1] + chain * y) not in friends_list and 0 <= position[0] + (
                    chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + chain * x, position[1] + chain * y) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_location
        enemies_list = black_location
    else:
        friends_list = black_location
        enemies_list = white_location
    for i in range(4):  # checking down up right left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = 1
        elif i == 1:
            x = -1
            y = 1
        elif i == 2:
            x = 1
            y = -1
        elif i == 3:
            x = -1
            y = -1

        while path:
            if (position[0] + chain * x, position[1] + chain * y) not in friends_list and 0 <= position[0] + chain * x <= 7 and 0 <= position[1] + chain * y <= 7:
                moves_list.append((position[0] + chain * x, position[1] + chain * y))
                if (position[0] + chain * x, position[1] + chain * y) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_knight(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_location
    else:
        friends_list = black_location

    for i in range(4):  # checking down up right left
        if i == 0:
            x = -1
            y = 1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        elif i == 3:
            x = 1
            y = -1
        if (position[0] + 1 * x, position[1] + 2 * y) not in friends_list and 0 <= position[0] + (1 * x) <= 7 and 0 <= position[1] + (2 * y) <= 7:
            moves_list.append((position[0] + 1 * x, position[1] + 2 * y))
        if (position[0] + 2 * x, position[1] + 1 * y) not in friends_list and 0 <= position[0] + (2 * x) <= 7 and 0 <= position[1] + (1 * y) <= 7:
            moves_list.append((position[0] + 2 * x, position[1] + 1 * y))
    return moves_list


# check valid moves for the piece selected
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

def draw_valid_moves(moves):
    if turn_step < 2:
        color = "red"
    else:
        color = "blue"
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 10)



# Main loop
black_options = check_options(black_pieces, black_location, 'black')
white_options = check_options(white_pieces, white_location, 'white')
running = True
while running:

    move = 1
    timer.tick(fps)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_cord = event.pos[0] // 100
            y_cord = event.pos[1] // 100
            click_coord = (x_cord, y_cord)



            if turn_step <= 1:
                if click_coord in white_location:
                    selection = white_location.index(click_coord)
                    selected_piece = black_pieces[selection]
                    if turn_step == 0:
                        turn_step = 1
                if click_coord in valid_moves and selection != 100:
                    white_location[selection] = click_coord

                    if selected_piece == 'pawn': ########################################## de mutat in urm if ca sa fac cu ceva x ceva adica takes!!!!!!!!!!!!!
                        print(f"{move}. {chr(8 - white_location[selection][0] + 64).lower()}{white_location[selection][1] + 1} ", end=" ")
                        move += 1
                    else:
                        print(f"{move}. {selected_piece[0].upper()}{chr(8 - white_location[selection][0] + 64).lower()}{white_location[selection][1] + 1} ", end=" ")
                        move += 1

                    if click_coord in black_location:
                        black_piece = black_location.index(click_coord)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_location.pop(black_piece)

                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')

                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coord in black_location:
                    selection = black_location.index(click_coord)
                    selected_piece = black_pieces[selection]   # "pawn" "rook" "knight" ...
                    if turn_step == 2:
                        turn_step = 3
                if click_coord in valid_moves and selection != 100:
                    black_location[selection] = click_coord

                    # print location on board
                    if selected_piece == 'pawn':
                        print(f"{chr(8 - black_location[selection][0] + 64).lower()}{black_location[selection][1] + 1}\n")
                    else:
                        print(f"{selected_piece[0].upper()}{chr(8 - black_location[selection][0] + 64).lower()}{black_location[selection][1] + 1}\n")

                    if click_coord in white_location:
                        white_piece = white_location.index(click_coord)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_location.pop(white_piece)

                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')

                    turn_step = 0
                    selection = 100
                    valid_moves = []

    draw_board()
    draw_pieces()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid_moves(valid_moves)
    pygame.display.flip()

pygame.quit()
sys.exit()
