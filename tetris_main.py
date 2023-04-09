import pygame
import sys
import random
import constants, tetrimino, board, draw, tetris_init
from pygame.locals import *
from board import add_to_board, remove_complete_lines

# Main function
def main():
    current_queue = tetris_init.generate_shape_queue()
    next_queue = tetris_init.generate_shape_queue()
    board = [[" " for _ in range(constants.GRID_WIDTH)] for _ in range(constants.GRID_HEIGHT)]
    if not current_queue:
        current_queue = next_queue
        next_queue = tetris_init.generate_shape_queue()
    shape, color = current_queue.pop(0)
    current_tetromino = tetrimino.Tetromino(shape, color, constants.GRID_WIDTH // 2 - 2, 0)
    timer = 0
    game_over = False
    


    # Create_ghost_tetrimino
    def create_ghost_tetrimino(current_tetromino, board):
        ghost_tetrimino = tetrimino.Tetromino(current_tetromino.shape, constants.GHOST_COLOR, current_tetromino.x, current_tetromino.y)
    
        while not tetrimino.check_collision(board, ghost_tetrimino.shape, ghost_tetrimino.x, ghost_tetrimino.y + 1):
            ghost_tetrimino.y += 1

        return ghost_tetrimino

    # Reset_current_tetromino
    def reset_current_tetromino(board, current_tetromino, current_queue, next_queue):
        board = add_to_board(board, current_tetromino)
        lines_cleared, board = remove_complete_lines(board)

        if not current_queue:
            current_queue = next_queue
            next_queue = tetris_init.generate_shape_queue()

        shape, color = current_queue.pop(0)

        current_tetromino = tetrimino.Tetromino(shape, color, constants.GRID_WIDTH // 2 - 2, 0)
        game_over = tetrimino.check_collision(board, current_tetromino.shape, current_tetromino.x, current_tetromino.y)

        return board, current_tetromino, game_over, current_queue, next_queue


    # While game is in session
    while not game_over:
        tetris_init.screen.fill(constants.WHITE)
        ghost_tetrimino = create_ghost_tetrimino(current_tetromino, board)
        draw.draw_ghost_tetromino(ghost_tetrimino)
        draw.draw_tetromino(current_tetromino)
        draw.draw_board(board)
        draw.draw_grid()

        
        # Handle user input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if not tetrimino.check_collision(board, current_tetromino.shape, current_tetromino.x - 1, current_tetromino.y):
                        current_tetromino.x -= 1
                if event.key == K_RIGHT:
                    if not tetrimino.check_collision(board, current_tetromino.shape, current_tetromino.x + 1, current_tetromino.y):
                        current_tetromino.x += 1
                if event.key == K_DOWN:
                    if not tetrimino.check_collision(board, current_tetromino.shape, current_tetromino.x, current_tetromino.y + 1):
                        current_tetromino.y += 1
                if event.key == K_UP:
                    while not tetrimino.check_collision(board, current_tetromino.shape, current_tetromino.x, current_tetromino.y + 1):
                        current_tetromino.y += 1
                    board, current_tetromino, game_over, current_queue, next_queue = reset_current_tetromino(board, current_tetromino, current_queue, next_queue)
                    timer = 0
                if event.key == K_LCTRL:
                    rotated_shape = tetrimino.rotate(current_tetromino.shape)
                    if not tetrimino.check_collision(board, rotated_shape, current_tetromino.x, current_tetromino.y):
                        current_tetromino.shape = rotated_shape
                if event.key == K_z:
                    rotated_shape = tetrimino.rotate(tetrimino.rotate(tetrimino.rotate(current_tetromino.shape)))
                    if not tetrimino.check_collision(board, rotated_shape, current_tetromino.x, current_tetromino.y):
                        current_tetromino.shape = rotated_shape
                

        # Update game state
        timer += tetris_init.clock.get_time() 
        if timer > constants.GAME_SPEED:
            if not tetrimino.check_collision(board, current_tetromino.shape, current_tetromino.x, current_tetromino.y + 1):
                current_tetromino.y += 1
            else:
                board, current_tetromino, game_over, current_queue, next_queue = reset_current_tetromino(board, current_tetromino, current_queue, next_queue)
            timer = 0

        pygame.display.flip()
        tetris_init.clock.tick(60)


#Run the main function
if __name__ == "__main__":
    main()

