# draw.py

import pygame
import constants
from tetrimino import Tetromino
# Draw all elements
def draw_game(game_state, screen):
    screen.fill(constants.WHITE)

    draw_grid(screen)
    draw_vertical_separator(screen)
    draw_board(game_state.board, screen)
    draw_ghost_tetromino(game_state.create_ghost_tetrimino(), screen)
    draw_tetromino(game_state.current_tetromino, screen)
    draw_piece_preview(game_state.current_queue + game_state.next_queue, screen, constants.PREVIEW_X, constants.PREVIEW_Y)
    draw_held_piece(game_state, screen)

# Draw Tetromino
def draw_tetromino(tetromino, screen, small=False, offsetX=0, offsetY=0):
    grid_size = constants.GRID_SIZE // 2 if small else constants.GRID_SIZE
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell == "X":
                pygame.draw.rect(screen, tetromino.color, (tetromino.x * grid_size + x * grid_size + offsetX, tetromino.y * grid_size + y * grid_size + offsetY, grid_size, grid_size), 0)
                pygame.draw.rect(screen, constants.BLACK, (tetromino.x * grid_size + x * grid_size + offsetX, tetromino.y * grid_size + y * grid_size + offsetY, grid_size, grid_size), 1)
      
# Draw Ghost Tetromino
def draw_ghost_tetromino(tetrimino, screen):
    for row in range(len(tetrimino.shape)):
        for col in range(len(tetrimino.shape[row])):
            if tetrimino.shape[row][col] == "X":
                color = tetrimino.color
                ghost_color = (color[0], color[1], color[2], 100)  # Set alpha value to 100 for transparency
                ghost_surface = pygame.Surface((constants.GRID_SIZE, constants.GRID_SIZE), pygame.SRCALPHA)  # Create a semi-transparent surface
                ghost_surface.fill(ghost_color)
                screen.blit(ghost_surface, (tetrimino.x * constants.GRID_SIZE + col * constants.GRID_SIZE, tetrimino.y * constants.GRID_SIZE + row * constants.GRID_SIZE))
                pygame.draw.rect(screen, constants.BLACK, (tetrimino.x * constants.GRID_SIZE + col * constants.GRID_SIZE, tetrimino.y * constants.GRID_SIZE + row * constants.GRID_SIZE, constants.GRID_SIZE, constants.GRID_SIZE), 1)

# Draw Board
def draw_board(board, screen):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell != " ":
                pygame.draw.rect(screen, cell, (x * constants.GRID_SIZE, y * constants.GRID_SIZE, constants.GRID_SIZE, constants.GRID_SIZE), 0)
                pygame.draw.rect(screen, constants.BLACK, (x * constants.GRID_SIZE, y * constants.GRID_SIZE, constants.GRID_SIZE, constants.GRID_SIZE), 1)

def draw_grid(screen):
    for x in range(0, constants.PLAYFIELD_WIDTH, constants.GRID_SIZE):
        pygame.draw.line(screen, constants.LIGHT_GREY, (x, 0), (x, constants.PLAYFIELD_HEIGHT))
    for y in range(0, constants.PLAYFIELD_HEIGHT, constants.GRID_SIZE):
        pygame.draw.line(screen, constants.LIGHT_GREY, (0, y), (constants.PLAYFIELD_WIDTH, y))

def draw_vertical_separator(screen):
    x = constants.PLAYFIELD_WIDTH
    pygame.draw.line(screen, constants.BLACK, (x, 0), (x, constants.PLAYFIELD_HEIGHT), 2)

def draw_piece_preview(queue, screen, x, y):
    for index, (shape, color) in enumerate(queue[:4]):
        tetromino = Tetromino(shape, color, 0, 0)  # Set x and y to 0
        draw_tetromino(tetromino, screen, small=True, offsetX=x, offsetY=y + index * 5 * constants.GRID_SIZE // 2)

def draw_held_piece(game_state, screen):
    if game_state.held_piece:
        x_offset = constants.HELD_X
        y_offset = constants.HELD_Y
        draw_tetromino(game_state.held_piece, screen, small=True, offsetX=x_offset, offsetY=y_offset)



