# tetris_user_input.py

from pygame.locals import *
import tetris_tetromino

# Handle User Input

def handle_user_input(game_state, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if not tetris_tetromino.check_collision(game_state.board, game_state.current_tetromino.shape, game_state.current_tetromino.x - 1, game_state.current_tetromino.y):
                    game_state.current_tetromino.x -= 1
            if event.key == K_RIGHT:
                if not tetris_tetromino.check_collision(game_state.board, game_state.current_tetromino.shape, game_state.current_tetromino.x + 1, game_state.current_tetromino.y):
                    game_state.current_tetromino.x += 1
            if event.key == K_DOWN:
                if not tetris_tetromino.check_collision(game_state.board, game_state.current_tetromino.shape, game_state.current_tetromino.x, game_state.current_tetromino.y + 1):
                    game_state.current_tetromino.y += 1
            if event.key == K_SPACE:
                while not tetris_tetromino.check_collision(game_state.board, game_state.current_tetromino.shape, game_state.current_tetromino.x, game_state.current_tetromino.y + 1):
                    game_state.current_tetromino.y += 1
                game_state.reset_current_tetromino()
                game_state.timer = 0
            if event.key == K_z or event.key == K_LCTRL:
                rotated_shape = tetris_tetromino.rotate(game_state.current_tetromino.shape)
                if not tetris_tetromino.check_collision(game_state.board, rotated_shape, game_state.current_tetromino.x, game_state.current_tetromino.y):
                    game_state.current_tetromino.shape = rotated_shape
            if event.key == K_UP:
                rotated_shape = tetris_tetromino.rotate(tetris_tetromino.rotate(tetris_tetromino.rotate(game_state.current_tetromino.shape)))
                if not tetris_tetromino.check_collision(game_state.board, rotated_shape, game_state.current_tetromino.x, game_state.current_tetromino.y):
                    game_state.current_tetromino.shape = rotated_shape
            if event.key == K_c or event.key == K_LSHIFT:
                game_state.hold_tetromino()