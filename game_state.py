import constants
import tetrimino
import tetris_init
from board import add_to_board, remove_complete_lines
from pygame.locals import *

class GameState:
    def __init__(self):
        self.current_queue = tetris_init.generate_shape_queue()
        self.next_queue = tetris_init.generate_shape_queue()
        self.board = [[" " for _ in range(constants.GRID_WIDTH)] for _ in range(constants.GRID_HEIGHT)]
        if not self.current_queue:
            self.current_queue = self.next_queue
            self.next_queue = tetris_init.generate_shape_queue()
        shape, color = self.current_queue.pop(0)
        self.current_tetromino = tetrimino.Tetromino(shape, color, constants.GRID_WIDTH // 2 - 2, 0)
        self.timer = 0
        self.game_over = False

    def create_ghost_tetrimino(self):
        ghost_tetrimino = tetrimino.Tetromino(self.current_tetromino.shape, constants.GHOST_COLOR, self.current_tetromino.x, self.current_tetromino.y)

        while not tetrimino.check_collision(self.board, ghost_tetrimino.shape, ghost_tetrimino.x, ghost_tetrimino.y + 1):
            ghost_tetrimino.y += 1

        return ghost_tetrimino

    def reset_current_tetromino(self):
        self.board = add_to_board(self.board, self.current_tetromino)
        lines_cleared, self.board = remove_complete_lines(self.board)

        if not self.current_queue:
            self.current_queue = self.next_queue
            self.next_queue = tetris_init.generate_shape_queue()

        shape, color = self.current_queue.pop(0)

        self.current_tetromino = tetrimino.Tetromino(shape, color, constants.GRID_WIDTH // 2 - 2, 0)
        self.game_over = tetrimino.check_collision(self.board, self.current_tetromino.shape, self.current_tetromino.x, self.current_tetromino.y)

    def handle_user_input(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if not tetrimino.check_collision(self.board, self.current_tetromino.shape, self.current_tetromino.x - 1, self.current_tetromino.y):
                    self.current_tetromino.x -= 1
            if event.key == K_RIGHT:
                if not tetrimino.check_collision(self.board, self.current_tetromino.shape, self.current_tetromino.x + 1, self.current_tetromino.y):
                    self.current_tetromino.x += 1
            if event.key == K_DOWN:
                if not tetrimino.check_collision(self.board, self.current_tetromino.shape, self.current_tetromino.x, self.current_tetromino.y + 1):
                    self.current_tetromino.y += 1
            if event.key == K_UP:
                while not tetrimino.check_collision(self.board, self.current_tetromino.shape, self.current_tetromino.x, self.current_tetromino.y + 1):
                    self.current_tetromino.y += 1
                self.reset_current_tetromino()
                self.timer = 0
            if event.key == K_LCTRL:
                rotated_shape = tetrimino.rotate(self.current_tetromino.shape)
                if not tetrimino.check_collision(self.board, rotated_shape, self.current_tetromino.x, self.current_tetromino.y):
                    self.current_tetromino.shape = rotated_shape
                if event.key == K_z:
                    rotated_shape = tetrimino.rotate(tetrimino.rotate(tetrimino.rotate(self.current_tetromino.shape)))
                    if not tetrimino.check_collision(self.board, rotated_shape, self.current_tetromino.x, self.current_tetromino.y):
                        self.current_tetromino.shape = rotated_shape

    def update(self):
        self.timer += tetris_init.clock.get_time() 
        if self.timer > constants.GAME_SPEED:
            if not tetrimino.check_collision(self.board, self.current_tetromino.shape, self.current_tetromino.x, self.current_tetromino.y + 1):
                self.current_tetromino.y += 1
            else:
                self.reset_current_tetromino()
            self.timer = 0
