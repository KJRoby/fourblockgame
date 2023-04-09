# tetrimino.py
import constants

# Tetromino class
class Tetromino:
    def __init__(self, shape, color, x, y):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y

    def reset_position(self):
        self.x = constants.GRID_WIDTH // 2 - 2
        self.y = 0


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



