# tetris_main.py

import pygame
import sys
from tetris_game_state import GameState
import tetris_draw
import tetris_constants

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((tetris_constants.WINDOW_WIDTH, tetris_constants.WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    
    # Initialize Game State
    game_state = GameState()
    
    # Main Game Loop
    while not game_state.game_over:
        screen.fill(tetris_constants.WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                sys.exit()

            game_state.handle_user_input(event)

        game_state.update(clock)
        tetris_draw.draw_game(game_state, screen)  
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
