# tetris_game_state.py

import random
import tetris_constants
import tetris_tetromino
from tetris_board import add_to_board, remove_complete_lines
from pygame.locals import *
from tetris_user_input import handle_user_input

class GameState:
    
    # Initialize Game State
    def __init__(self):
        self.current_queue = self.generate_shape_queue()
        self.next_queue = self.generate_shape_queue()
        self.board = [[" " for _ in range(tetris_constants.GRID_WIDTH)] for _ in range(tetris_constants.GRID_HEIGHT)]
        if not self.current_queue:
            self.current_queue = self.next_queue
            self.next_queue = self.generate_shape_queue()
        shape, color, name = self.current_queue.pop(0)
        self.current_tetromino = tetris_tetromino.Tetromino(shape, color, tetris_constants.GRID_WIDTH // 2 - 2, 0, name)
        self.timer = 0
        self.game_over = False
        self.held_piece = None
        self.swap_allowed = True

    # Fills a "bag" with all seven tetrominoes and then randomly selects one
    def generate_shape_queue(self):
        shape_queue = random.sample(tetris_constants.TETROMINO_VARIANTS, len(tetris_constants.TETROMINO_VARIANTS))
        return shape_queue
    
    # Creates a preview of where the current tetromino will land
    def create_ghost_tetrimino(self):
        ghost_tetrimino = tetris_tetromino.Tetromino(self.current_tetromino.shape, self.current_tetromino.color, self.current_tetromino.x, self.current_tetromino.y, self.current_tetromino.name)

        while not tetris_tetromino.check_collision(self.board, ghost_tetrimino.shape, ghost_tetrimino.x, ghost_tetrimino.y + 1):
            ghost_tetrimino.y += 1

        return ghost_tetrimino

    # Reset Current Tetromino (Done after Tetromino is placed or hard dropped)
    def reset_current_tetromino(self):
        self.board = add_to_board(self.board, self.current_tetromino)
        lines_cleared, self.board = remove_complete_lines(self.board)

        if not self.current_queue:
            self.current_queue = self.next_queue
            self.next_queue = self.generate_shape_queue()

        shape, color, name = self.current_queue.pop(0)

        self.current_tetromino = tetris_tetromino.Tetromino(shape, color, tetris_constants.GRID_WIDTH // 2 - 2, 0, name)
        self.game_over = tetris_tetromino.check_collision(self.board, self.current_tetromino.shape, self.current_tetromino.x, self.current_tetromino.y)
        self.swap_allowed = True
        
    # Hold Tetromino (Done When user presses "Left Shift")
    def hold_tetromino(self):
        if not self.swap_allowed:
            return

        if self.held_piece is None:
            self.held_piece = self.current_tetromino
            if not self.current_queue:
                self.current_queue = self.next_queue
                self.next_queue = self.generate_shape_queue()
            shape, color, name = self.current_queue.pop(0)
            self.current_tetromino = tetris_tetromino.Tetromino(shape, color, tetris_constants.GRID_WIDTH // 2 - 2, 0, name)
            self.held_piece.reset_position()
        else:
            self.held_piece, self.current_tetromino = self.current_tetromino, self.held_piece
            self.current_tetromino.reset_position()
            self.held_piece.reset_position()

        self.swap_allowed = False

    # Handle User Input
    def handle_user_input(self, event):
        handle_user_input(self, event)

    # Update Game State (Timing and Game Logic)
    def update(self, clock):
        self.timer += clock.get_time() 
        if self.timer > tetris_constants.GAME_SPEED:
            if not tetris_tetromino.check_collision(self.board, self.current_tetromino.shape, self.current_tetromino.x, self.current_tetromino.y + 1):
                self.current_tetromino.y += 1
            else:
                self.reset_current_tetromino()
            self.timer = 0
