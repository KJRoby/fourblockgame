import pygame
import constants
import game_state
# Draw Tetromino



def draw_game(game_state, screen):
    screen.fill(constants.WHITE)
    
    draw_grid(screen)
    draw_vertical_separator(screen)
    draw_board(game_state.board, screen)
    draw_tetromino(game_state.current_tetromino, screen)
    draw_tetromino(game_state.create_ghost_tetrimino(), screen)



def draw_tetromino(tetromino, screen):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell == "X":
                pygame.draw.rect(screen, tetromino.color, (tetromino.x * constants.GRID_SIZE + x * constants.GRID_SIZE, tetromino.y * constants.GRID_SIZE + y * constants.GRID_SIZE, constants.GRID_SIZE, constants.GRID_SIZE), 0)
                pygame.draw.rect(screen, constants.BLACK, (tetromino.x * constants.GRID_SIZE + x * constants.GRID_SIZE, tetromino.y * constants.GRID_SIZE + y * constants.GRID_SIZE, constants.GRID_SIZE, constants.GRID_SIZE), 1)
                
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
