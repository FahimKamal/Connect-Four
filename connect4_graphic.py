"""
Connect Four (pygame)
Create by: Fahim Kamal
Date: 20.01.2020
"""
import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7
pygame.init()

def create_board():
    """Create the matrix for the game"""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[5][col] == 0


def print_board(board):
    print(np.flip(board, 0))


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def wining_board(board, piece):
    # Check all the horizontal locations
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                return True

    # Check all the vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                return True

        # Check all positively diagonals locations
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][
                            c + 3] == piece:
                    return True

        # Check all negatively diagonals locations
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][
                            c + 3] == piece:
                    return True


# Screen elements
square_size = 50
width = COLUMN_COUNT * square_size
height = (ROW_COUNT + 1) * square_size
screen_size = (width, height)
font = pygame.font.SysFont('monospace', 30)

# set color (R, G, B)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
RADIUS = (square_size // 2) - 3

def draw_board(board):
    """Fucntion will draw the game board in the screen"""
    board = np.flip(board, 0)
    for r in range(ROW_COUNT-1, -1, -1):
        for c in range(COLUMN_COUNT):
            pygame.draw.rect(screen, BLUE, (c*square_size, r*square_size+square_size, square_size, square_size))
            if board[r][c] == 0:
                pygame.draw.circle(screen, BLACK, (int(c*square_size+ square_size / 2), int(r*square_size+square_size+square_size /2)), RADIUS)
            elif board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*square_size+ square_size / 2), int(r*square_size+square_size+square_size /2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*square_size+ square_size / 2), int(r*square_size+square_size+square_size /2)), RADIUS)
    # Update the screen
    pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

# set Screen

screen = pygame.display.set_mode(screen_size)
draw_board(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():

        # to close the game
        if event.type == pygame.QUIT:
            sys.exit()
        # track the mouse movement in the screen
        if event.type == pygame.MOUSEMOTION:
            # Will delete the previous circle so the new circle can be seen
            pygame.draw.rect(screen, BLACK, (0, 0, width, square_size))
            position_x = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (position_x, square_size // 2), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (position_x, square_size // 2), RADIUS)
        pygame.display.update()

        # If click on the mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Mouse button clicked')
            print(event.pos)
            pygame.draw.rect(screen, BLACK, (0, 0, width, square_size))
            # Ask for player 1 input
            if turn is 0:
                # get x position of the mouse location
                position_x = event.pos[0]
                col = position_x // square_size
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    if wining_board(board, 1):
                        print('Player 1 wins!!!')
                        label = font.render('Player 1 wins!!', True, RED)
                        screen.blit(label, (40, 10))
                        game_over = True
                else:
                    print('column is full')

            # Ask for player 2 input
            else:
                # get x position of the mouse location
                position_x = event.pos[0]
                col = position_x // square_size
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if wining_board(board, 2):
                        print('Player 2 wins!!!')
                        label = font.render('Player 2 wins!!', True, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True
                else:
                    print('column is full')

            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)
