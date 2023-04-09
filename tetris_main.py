# tetris_main.py

import pygame
import sys
from game_state import GameState
import draw
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
        draw.draw_game(game_state, screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
