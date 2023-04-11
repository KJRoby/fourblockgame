# draw.py

import pygame
import tetris_constants
from tetris_tetromino import Tetromino
# Draw all elements
def draw_game(game_state, screen):
    screen.fill(tetris_constants.WHITE)

    draw_grid(screen)
    draw_vertical_separator(screen)
    draw_board(game_state.board, screen)
    draw_ghost_tetromino(game_state.create_ghost_tetrimino(), screen)
    draw_tetromino(game_state.current_tetromino, screen)
    draw_piece_preview(game_state.current_queue + game_state.next_queue, screen, tetris_constants.PREVIEW_X, tetris_constants.PREVIEW_Y)
    draw_held_piece(game_state, screen)

# Draw Tetromino
def draw_tetromino(tetromino, screen, small=False, offsetX=0, offsetY=0):
    grid_size = tetris_constants.GRID_SIZE // 2 if small else tetris_constants.GRID_SIZE
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell == "X":
                pygame.draw.rect(screen, tetromino.color, (tetromino.x * grid_size + x * grid_size + offsetX, tetromino.y * grid_size + y * grid_size + offsetY, grid_size, grid_size), 0)
                pygame.draw.rect(screen, tetris_constants.BLACK, (tetromino.x * grid_size + x * grid_size + offsetX, tetromino.y * grid_size + y * grid_size + offsetY, grid_size, grid_size), 1)
      
# Draw Ghost Tetromino
def draw_ghost_tetromino(tetrimino, screen):
    for row in range(len(tetrimino.shape)):
        for col in range(len(tetrimino.shape[row])):
            if tetrimino.shape[row][col] == "X":
                color = tetrimino.color
                ghost_color = (color[0], color[1], color[2], 100)  # Set alpha value to 100 for transparency
                ghost_surface = pygame.Surface((tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE), pygame.SRCALPHA)  # Create a semi-transparent surface
                ghost_surface.fill(ghost_color)
                screen.blit(ghost_surface, (tetrimino.x * tetris_constants.GRID_SIZE + col * tetris_constants.GRID_SIZE, tetrimino.y * tetris_constants.GRID_SIZE + row * tetris_constants.GRID_SIZE))
                pygame.draw.rect(screen, tetris_constants.BLACK, (tetrimino.x * tetris_constants.GRID_SIZE + col * tetris_constants.GRID_SIZE, tetrimino.y * tetris_constants.GRID_SIZE + row * tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE), 1)

# Draw Board
def draw_board(board, screen):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell != " ":
                pygame.draw.rect(screen, cell, (x * tetris_constants.GRID_SIZE, y * tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE), 0)
                pygame.draw.rect(screen, tetris_constants.BLACK, (x * tetris_constants.GRID_SIZE, y * tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE), 1)

def draw_grid(screen):
    for x in range(0, tetris_constants.PLAYFIELD_WIDTH, tetris_constants.GRID_SIZE):
        pygame.draw.line(screen, tetris_constants.LIGHT_GREY, (x, 0), (x, tetris_constants.PLAYFIELD_HEIGHT))
    for y in range(0, tetris_constants.PLAYFIELD_HEIGHT, tetris_constants.GRID_SIZE):
        pygame.draw.line(screen, tetris_constants.LIGHT_GREY, (0, y), (tetris_constants.PLAYFIELD_WIDTH, y))

def draw_vertical_separator(screen):
    x = tetris_constants.PLAYFIELD_WIDTH
    pygame.draw.line(screen, tetris_constants.BLACK, (x, 0), (x, tetris_constants.PLAYFIELD_HEIGHT), 2)

def draw_piece_preview(queue, screen, x, y):
    for index, (shape, color) in enumerate(queue[:4]):
        tetromino = Tetromino(shape, color, 0, 0)  # Set x and y to 0
        draw_tetromino(tetromino, screen, small=True, offsetX=x, offsetY=y + index * 5 * tetris_constants.GRID_SIZE // 2)

def draw_held_piece(game_state, screen):
    if game_state.held_piece:
        x_offset = tetris_constants.HELD_X
        y_offset = tetris_constants.HELD_Y
        draw_tetromino(game_state.held_piece, screen, small=True, offsetX=x_offset, offsetY=y_offset)



