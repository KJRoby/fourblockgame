# tetromino.py
import tetris_constants

# Tetromino class
class Tetromino:
    def __init__(self, shape, color, x, y, name, rotation=0):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y
        self.name = name
        self.rotation = rotation

    def reset_position(self):
        self.x = tetris_constants.GRID_WIDTH // 2 - 2
        self.y = 0


# Check collision
def check_collision(board, shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] == "X" and (y + row >= len(board) or x + col < 0 or x + col >= len(board[0]) or board[y + row][x + col] != " "):
                return True
    return False

# Rotate shape
def rotate(shape, clockwise=True):
    if clockwise:
        return ["".join([shape[y][x] for y in range(len(shape)-1, -1, -1)]) for x in range(len(shape[0]))]
    else:
        return ["".join([shape[y][x] for y in range(len(shape))]) for x in range(len(shape[0]) - 1, -1, -1)]




