# tetris_srs.py

from tetris_tetromino import Tetromino, rotate, check_collision

# SRS rotation offsets for Tetriminos
# Format: {shape: [[(x, y), (x, y), (x, y), (x, y)], ...], ...}
# Each tuple (x, y) represents the offset from the current position
# Each list of tuples represents a possible rotation
SRS_OFFSETS = {
    "I": [
        [(-1, 0), (-1, 1), (0, -2), (-1, -2)],  # 0 >> R
        [(1, 0), (1, -1), (0, 2), (1, 2)],      # R >> 2
        [(1, 0), (1, 1), (0, -2), (1, -2)],     # 2 >> L
        [(-1, 0), (-1, -1), (0, 2), (-1, 2)],   # L >> 0
    ],

    "O": [
        [(0, 0)],
        [(0, 0)],
        [(0, 0)],
        [(0, 0)],
    ],
    "T": [
        [(0, 0), (1, 0), (0, 1), (-1, 1)],
        [(0, 0), (0, 1), (1, 1), (1, 0)],
        [(0, 0), (-1, 0), (0, 1), (1, 1)],
        [(0, 0), (0, 1), (-1, 1), (-1, 0)],
    ],
    "S": [
        [(0, 0), (1, 0), (0, 1), (-1, 1)],
        [(0, 0), (0, 1), (1, 1), (1, 0)],
        [(0, 0), (-1, 0), (0, 1), (1, 1)],
        [(0, 0), (0, 1), (-1, 1), (-1, 0)],
    ],
    "Z": [
        [(0, 0), (1, 0), (0, 1), (-1, 1)],
        [(0, 0), (0, 1), (1, 1), (1, 0)],
        [(0, 0), (-1, 0), (0, 1), (1, 1)],
        [(0, 0), (0, 1), (-1, 1), (-1, 0)],
    ],
    "J": [
        [(0, 0), (1, 0), (0, 1), (-1, 1)],
        [(0, 0), (0, 1), (1, 1), (1, 0)],
        [(0, 0), (-1, 0), (0, 1), (1, 1)],
        [(0, 0), (0, 1), (-1, 1), (-1, 0)],
    ],
    "L": [
        [(0, 0), (1, 0), (0, 1), (-1, 1)],
        [(0, 0), (0, 1), (1, 1), (1, 0)],
        [(0, 0), (-1, 0), (0, 1), (1, 1)],
        [(0, 0), (0, 1), (-1, 1), (-1, 0)],
    ], 
}

# Rotate a tetromino using SRS rotation offsets
def rotate_srs(tetromino, board, clockwise):
    shape_name = tetromino.name

    if shape_name == "O": # Temporary fix for O tetromino
        return tetromino

    if shape_name not in SRS_OFFSETS:
        return tetromino

    offsets = SRS_OFFSETS[shape_name]
    rotation_index = (tetromino.rotation + (1 if clockwise else -1)) % len(offsets)

    rotated_shape = rotate(tetromino.shape)
    for i, offset in enumerate(offsets[rotation_index]):
        test_x = tetromino.x + offset[0]
        test_y = tetromino.y + offset[1]
        if not check_collision(board, rotated_shape, test_x, test_y):
            rotated_tetromino = Tetromino(rotated_shape, tetromino.color, test_x, test_y, shape_name, rotation_index)
            return rotated_tetromino

    return None
