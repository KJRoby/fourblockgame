import pygame
import sys
from game_state import GameState
from draw import draw_board, draw_tetromino, draw_ghost_tetromino, draw_grid
from tetris_init import screen, clock
import constants

def main():
    pygame.init()
    game_state = GameState()
    
    while not game_state.game_over:
        screen.fill(constants.WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            game_state.handle_user_input(event)

        game_state.update()
        draw_board(game_state.board)
        ghost_tetromino = game_state.create_ghost_tetrimino()
        draw_ghost_tetromino(ghost_tetromino)
        draw_tetromino(game_state.current_tetromino)
        draw_grid()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
