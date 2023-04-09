# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
PLAYFIELD_WIDTH = 400
PLAYFIELD_HEIGHT = 800
GRID_SIZE = 40
GRID_WIDTH = PLAYFIELD_WIDTH // GRID_SIZE
GRID_HEIGHT = PLAYFIELD_HEIGHT // GRID_SIZE
GAME_SPEED = 1000

# Tetromino colors
I_COLOR = (0, 255, 255)             # Cyan
J_COLOR = (0, 0, 255)               # Blue
L_COLOR = (255, 165, 0)             # Orange
O_COLOR = (255, 255, 0)             # Yellow
S_COLOR = (0, 255, 0)               # Green
T_COLOR = (128, 0, 128)             # Violet
Z_COLOR = (255, 0, 0)               # Red
GHOST_COLOR = (128, 128, 128, 77)   #Transparent Grey

# Board Colors
WHITE = (255, 255, 255)
LIGHT_GREY = (211, 211, 211)
BLACK = (0, 0, 0)

# Tetromino shapes and their colors
SHAPES_COLORS = [
    ([
        "  X ",
        "  X ",
        "  X ",
        "  X ",
    ], I_COLOR),
    ([
        " XX ",
        " XX ",
    ], O_COLOR),
    ([
        "X  ",
        "XXX",
    ], L_COLOR),
    ([
        "  X",
        "XXX",
    ], J_COLOR),
    ([
        " XX",
        "XX ",
    ], S_COLOR),
    ([
        "XX ",
        " XX",
    ], Z_COLOR),
    ([
        " X ",
        "XXX",
    ], T_COLOR),
]
