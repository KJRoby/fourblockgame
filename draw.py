import pygame
import sys
import constants, tetris_init

# Draw Tetromino
def draw_tetromino(tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell == "X":
                pygame.draw.rect(tetris_init.screen, tetromino.color, (tetromino.x * constants.GRID_SIZE + x * constants.GRID_SIZE, tetromino.y * constants.GRID_SIZE + y * constants.GRID_SIZE, constants.GRID_SIZE, constants.GRID_SIZE), 0)
                pygame.draw.rect(tetris_init.screen, constants.BLACK, (tetromino.x * constants.GRID_SIZE + x * constants.GRID_SIZE, tetromino.y * constants.GRID_SIZE + y * constants.GRID_SIZE, constants.GRID_SIZE, constants.GRID_SIZE), 1)
                
# Draw Ghost Tetromino
def draw_ghost_tetromino(tetrimino):
    for row in range(len(tetrimino.shape)):
        for col in range(len(tetrimino.shape[row])):
            if tetrimino.shape[row][col] == "X":
                color = tetrimino.color
                ghost_color = (color[0], color[1], color[2], 100)  # Set alpha value to 100 for transparency
                ghost_surface = pygame.Surface((constants.GRID_SIZE, constants.GRID_SIZE), pygame.SRCALPHA)  # Create a semi-transparent surface
                ghost_surface.fill(ghost_color)
                tetris_init.screen.blit(ghost_surface, (tetrimino.x * constants.GRID_SIZE + col * constants.GRID_SIZE, tetrimino.y * constants.GRID_SIZE + row * constants.GRID_SIZE))
                pygame.draw.rect(tetris_init.screen, constants.BLACK, (tetrimino.x * constants.GRID_SIZE + col * constants.GRID_SIZE, tetrimino.y * constants.GRID_SIZE + row * constants.GRID_SIZE, constants.GRID_SIZE, constants.GRID_SIZE), 1)

# Draw Board
def draw_board(board):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell != " ":
                pygame.draw.rect(tetris_init.screen, cell, (x * constants.GRID_SIZE, y * constants.GRID_SIZE, constants.GRID_SIZE, constants.GRID_SIZE), 0)
                pygame.draw.rect(tetris_init.screen, constants.BLACK, (x * constants.GRID_SIZE, y * constants.GRID_SIZE, constants.GRID_SIZE, constants.GRID_SIZE), 1)

# Draw Grid
def draw_grid():
    for x in range(0, constants.WINDOW_WIDTH, constants.GRID_SIZE):
        pygame.draw.line(tetris_init.screen, constants.LIGHT_GREY, (x, 0), (x, constants.WINDOW_HEIGHT))
    for y in range(0, constants.WINDOW_HEIGHT, constants.GRID_SIZE):
        pygame.draw.line(tetris_init.screen, constants.LIGHT_GREY, (0, y), (constants.WINDOW_WIDTH, y))

