# tetris_tetromino.py
import tetris_constants

# Tetromino class
class Tetromino:
    def __init__(self, shape, color, x, y, name):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y
        self.name = name

    def reset_position(self):
        self.x = tetris_constants.GRID_WIDTH // 2 - 2
        self.y = 0

    def get_dimensions(self, shape=None):
        if shape is None:
            shape = self.shape
        width = max(len(row) for row in shape)
        height = len(shape)
        return width, height    


# Check collision
def check_collision(board, shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] == "X" and (y + row >= len(board) or x + col < 0 or x + col >= len(board[0]) or board[y + row][x + col] != " "):
                return True
    return False

# Rotate shape
def rotate(shape):
    return ["".join([shape[y][x] for y in range(len(shape))]) for x in range(len(shape[0]) - 1, -1, -1)]



