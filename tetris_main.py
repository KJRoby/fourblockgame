import pygame
import sys
from game_state import GameState
from draw import draw_board, draw_tetromino, draw_ghost_tetromino, draw_grid
import constants

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    
    # Initialize Game State
    game_state = GameState()
    
    # Main Game Loop
    while not game_state.game_over:
        screen.fill(constants.WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            game_state.handle_user_input(event)

        game_state.update(clock)
        draw_board(game_state.board, screen)
        ghost_tetromino = game_state.create_ghost_tetrimino()
        draw_ghost_tetromino(ghost_tetromino, screen)
        draw_tetromino(game_state.current_tetromino, screen)
        draw_grid(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
