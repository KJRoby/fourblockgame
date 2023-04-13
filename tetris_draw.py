# tetris_draw.py

import pygame
import tetris_constants
from tetris_tetromino import Tetromino

# Draw all elements
def draw_game(game_state, screen):
    screen.fill(tetris_constants.WHITE) # Fill screen with black

    draw_playfield(screen)
    draw_vertical_separator(screen)
    draw_board(game_state.board, screen)
    draw_ghost_tetromino(game_state.create_ghost_tetrimino(), screen)
    draw_tetromino(game_state.current_tetromino, screen)
    draw_preview_box(screen)
    draw_piece_preview(game_state.current_queue + game_state.next_queue, screen, tetris_constants.PREVIEW_X, tetris_constants.PREVIEW_Y, game_state.current_tetromino.name)
    draw_held_piece_box(screen)
    draw_held_piece(game_state, screen)

def draw_tetromino(tetromino, screen, small=False, offsetX=0, offsetY=0, center=False):
    grid_size = tetris_constants.GRID_SIZE // 2 if small else tetris_constants.GRID_SIZE
    # Create a new list of rows with at least one occupied cell if small is True
    shape_to_draw = [row for row in tetromino.shape if any(cell == 'X' for cell in row)] if small else tetromino.shape
    
    if center:
        width, height = tetromino.get_dimensions(shape_to_draw)  # Pass the trimmed shape to get_dimensions
        offsetX += (tetris_constants.HELD_BOX_WIDTH - (width * grid_size)) // 2
        offsetY += (tetris_constants.HELD_BOX_HEIGHT - (height * grid_size)) // 2

    for y, row in enumerate(shape_to_draw):
        for x, cell in enumerate(row):
            if cell == "X":
                pygame.draw.rect(screen, tetromino.color, (tetromino.x * grid_size + x * grid_size + offsetX, tetromino.y * grid_size + y * grid_size + offsetY, grid_size, grid_size), 0)  # Draw a filled mino.
                pygame.draw.rect(screen, tetris_constants.BLACK, (tetromino.x * grid_size + x * grid_size + offsetX, tetromino.y * grid_size + y * grid_size + offsetY, grid_size, grid_size), 1)  # Draw a mino outline.



      
# Draw Ghost Tetromino
def draw_ghost_tetromino(tetrimino, screen):
    for row in range(len(tetrimino.shape)):
        for col in range(len(tetrimino.shape[row])):
            if tetrimino.shape[row][col] == "X":
                color = tetrimino.color
                ghost_color = (color[0], color[1], color[2], 100)  # Create a semi-transparent color
                ghost_surface = pygame.Surface((tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE), pygame.SRCALPHA)  # Create a semi-transparent surface
                ghost_surface.fill(ghost_color)
                screen.blit(ghost_surface, (tetrimino.x * tetris_constants.GRID_SIZE + col * tetris_constants.GRID_SIZE, tetrimino.y * tetris_constants.GRID_SIZE + row * tetris_constants.GRID_SIZE))
                pygame.draw.rect(screen, color, (tetrimino.x * tetris_constants.GRID_SIZE + col * tetris_constants.GRID_SIZE, tetrimino.y * tetris_constants.GRID_SIZE + row * tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE), 1)

# Draw Board

def draw_board(board, screen):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell != " ":
                pygame.draw.rect(screen, cell, (x * tetris_constants.GRID_SIZE, y * tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE), 0)
                pygame.draw.rect(screen, tetris_constants.BLACK, (x * tetris_constants.GRID_SIZE, y * tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE, tetris_constants.GRID_SIZE), 1) 
               

def draw_playfield(screen):
    # Fill the playfield area with black color
    pygame.draw.rect(screen, tetris_constants.BLACK, (0, 0, tetris_constants.PLAYFIELD_WIDTH, tetris_constants.PLAYFIELD_HEIGHT))
    # Draw grid lines
    for x in range(0, tetris_constants.PLAYFIELD_WIDTH, tetris_constants.GRID_SIZE):
        pygame.draw.line(screen, tetris_constants.DARK_GREY, (x, 0), (x, tetris_constants.PLAYFIELD_HEIGHT))
    for y in range(0, tetris_constants.PLAYFIELD_HEIGHT, tetris_constants.GRID_SIZE):
        pygame.draw.line(screen, tetris_constants.DARK_GREY, (0, y), (tetris_constants.PLAYFIELD_WIDTH, y))


def draw_vertical_separator(screen):
    x = tetris_constants.PLAYFIELD_WIDTH
    pygame.draw.line(screen, tetris_constants.BLACK, (x, 0), (x, tetris_constants.PLAYFIELD_HEIGHT), 2)

# The "Hacky" way to draw the preview box (because I can't be arsed to do the math to make it work like the held box)
def draw_piece_preview(queue, screen, x, y, name):
    for index, (shape, color, name) in enumerate(queue[:6]):
        tetromino = Tetromino(shape, color, 0, 0, name)  # Set x and y to 0

        # Centering adjustments for O and I pieces
        x_offset = x # 480
        y_offset = (y + 10) + index * 5 * tetris_constants.GRID_SIZE // 2 # (80 + 10) + [index] * 5 * 20 // 2 
        if name == "O":
            x_offset += tetris_constants.GRID_SIZE // 4 # 
            y_offset += tetris_constants.GRID_SIZE // 4
        elif name == "I":
            x_offset -= tetris_constants.GRID_SIZE // 4

        draw_tetromino(tetromino, screen, small=True, offsetX=x_offset, offsetY=y_offset)

# The "Proper" way to center the pieces in the preview box (but it doesn't work)
#def draw_piece_preview(queue, screen, x, y, name):
    #for index, (shape, color, name) in enumerate(queue[:6]):
        #tetromino = Tetromino(shape, color, 0, 0, name)  # Set x and y to 0

        # Centering adjustments for all pieces
        #width, height = tetromino.get_dimensions()
        #x_offset = x + (tetris_constants.PREVIEW_BOX_WIDTH - (width * (tetris_constants.GRID_SIZE // 2))) // 2
        #y_offset = y + (tetris_constants.PREVIEW_BOX_HEIGHT // 6 * index) - (height * (tetris_constants.GRID_SIZE // 2)) // 2 

        #draw_tetromino(tetromino, screen, small=True, offsetX=x_offset, offsetY=y_offset)



def draw_preview_box(screen):
    # Fill the black box with dark grey color
    pygame.draw.rect(screen, tetris_constants.DARK_GREY, (tetris_constants.PREVIEW_BOX_X, tetris_constants.PREVIEW_BOX_Y, tetris_constants.PREVIEW_BOX_WIDTH, tetris_constants.PREVIEW_BOX_HEIGHT))

    # Draw a black border around the preview box
    pygame.draw.rect(screen, tetris_constants.BLACK, (tetris_constants.PREVIEW_BOX_X, tetris_constants.PREVIEW_BOX_Y, tetris_constants.PREVIEW_BOX_WIDTH, tetris_constants.PREVIEW_BOX_HEIGHT), tetris_constants.PREVIEW_BOX_BORDER)

    # Draw caption "NEXT"
    font = pygame.font.Font(None, tetris_constants.CAPTION_FONT_SIZE)
    text_surface = font.render("NEXT", True, tetris_constants.CAPTION_FONT_COLOR)
    text_rect = text_surface.get_rect(center=(tetris_constants.PREVIEW_BOX_X + tetris_constants.PREVIEW_BOX_WIDTH // 2, tetris_constants.PREVIEW_BOX_Y - tetris_constants.GRID_SIZE))
    screen.blit(text_surface, text_rect)


# Draw Held Piece
def draw_held_piece(game_state, screen):
    if game_state.held_piece:
        x_offset = tetris_constants.HELD_BOX_X - (3 * (tetris_constants.GRID_SIZE // 2))
        y_offset = tetris_constants.HELD_BOX_Y
        draw_tetromino(game_state.held_piece, screen, small=True, offsetX=x_offset, offsetY=y_offset, center=True)



def draw_held_piece_box(screen):
    # Draw black box
    # Fill the black box with black color
    pygame.draw.rect(screen, tetris_constants.DARK_GREY, (tetris_constants.HELD_BOX_X, tetris_constants.HELD_BOX_Y, tetris_constants.HELD_BOX_WIDTH, tetris_constants.HELD_BOX_HEIGHT))

    # Draw a grid similar to the playfield over held piece box but with black lines for x and y axis and area divided by 2 for x and y axis to match the smaller size of the held minos. 
    #for x in range(tetris_constants.HELD_BOX_X, tetris_constants.HELD_BOX_X + tetris_constants.HELD_BOX_WIDTH + tetris_constants.GRID_SIZE // 2, tetris_constants.GRID_SIZE // 2):
        #pygame.draw.line(screen, tetris_constants.BLACK, (x, tetris_constants.HELD_BOX_Y), (x, tetris_constants.HELD_BOX_Y + tetris_constants.HELD_BOX_HEIGHT))
    #for y in range(tetris_constants.HELD_BOX_Y, tetris_constants.HELD_BOX_Y + tetris_constants.HELD_BOX_HEIGHT + tetris_constants.GRID_SIZE // 2, tetris_constants.GRID_SIZE // 2):
        #pygame.draw.line(screen, tetris_constants.BLACK, (tetris_constants.HELD_BOX_X, y), (tetris_constants.HELD_BOX_X + tetris_constants.HELD_BOX_WIDTH, y)) # Unused

    # Draw a black border around the held piece box
    pygame.draw.rect(screen, tetris_constants.BLACK, (tetris_constants.HELD_BOX_X, tetris_constants.HELD_BOX_Y, tetris_constants.HELD_BOX_WIDTH, tetris_constants.HELD_BOX_HEIGHT), tetris_constants.HELD_BOX_BORDER)

    

    # Draw caption "HOLD"
    font = pygame.font.Font(None, tetris_constants.CAPTION_FONT_SIZE)
    text_surface = font.render("HOLD", True, tetris_constants.CAPTION_FONT_COLOR)
    text_rect = text_surface.get_rect(center=(tetris_constants.HELD_BOX_X + tetris_constants.HELD_BOX_WIDTH // 2, tetris_constants.HELD_BOX_Y - tetris_constants.GRID_SIZE))
    screen.blit(text_surface, text_rect)