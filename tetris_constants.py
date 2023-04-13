# tetris_constants.py 



# --Window and grid constants--
# Window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# Playfield
PLAYFIELD_WIDTH = 400
PLAYFIELD_HEIGHT = 800

# Grid
GRID_SIZE = 40
GRID_WIDTH = PLAYFIELD_WIDTH // GRID_SIZE
GRID_HEIGHT = PLAYFIELD_HEIGHT // GRID_SIZE

# Next Piece Preview Box
PREVIEW_X = PLAYFIELD_WIDTH + GRID_SIZE * 2
PREVIEW_Y = GRID_SIZE * 2
PREVIEW_BOX_X = PREVIEW_X - GRID_SIZE // 2
PREVIEW_BOX_Y = PREVIEW_Y - GRID_SIZE // 2
PREVIEW_BOX_WIDTH = 5 * GRID_SIZE // 2
PREVIEW_BOX_HEIGHT = 6 * 5 * GRID_SIZE // 2 + GRID_SIZE
PREVIEW_BOX_BORDER = 4

# Held Piece Box
HELD_X = PREVIEW_X + PREVIEW_BOX_WIDTH + GRID_SIZE * 2
HELD_Y = GRID_SIZE * 2
HELD_BOX_X = HELD_X - GRID_SIZE // 2
HELD_BOX_Y = HELD_Y - GRID_SIZE // 2
HELD_BOX_HEIGHT = 5 * GRID_SIZE // 2
HELD_BOX_WIDTH = 5 * GRID_SIZE // 2
HELD_BOX_BORDER = 4


# --Fonts--
CAPTION_FONT_SIZE = 24
CAPTION_FONT_COLOR = (0, 0, 0)  # Black

# --Colors--
# Tetromino colors
I_COLOR = (0, 255, 255)             # Cyan
J_COLOR = (0, 0, 255)               # Blue
L_COLOR = (255, 165, 0)             # Orange
O_COLOR = (255, 255, 0)             # Yellow
S_COLOR = (0, 255, 0)               # Green
T_COLOR = (128, 0, 128)             # Violet
Z_COLOR = (255, 0, 0)               # Red
GHOST_COLOR = (200, 200, 200, 255)   #Transparent Grey
HELD_COLOR = (255, 110, 199)        #Neon Pink

# Board Colors
WHITE = (255, 255, 255)
DARK_GREY = (50, 50, 50)
BLACK = (0, 0, 0)

#--Game constants--
# Game speed 
GAME_SPEED = 1000
# Tetromino shapes and their colors
TETROMINO_VARIANTS = [
    ([
        "    ",
        "XXXX",
        "    ",
        "    ",
    ], I_COLOR),
    ([
        "XX",
        "XX"
    ], O_COLOR),
    ([
        "X  ",
        "XXX",
        "   ",
    ], J_COLOR),
    ([
        "  X",
        "XXX",
        "   ",
    ], L_COLOR),
    ([
        " XX",
        "XX ",
        "   ",
    ], S_COLOR),
    ([
        "XX ",
        " XX",
        "   ",
    ], Z_COLOR),
    ([
        " X ",
        "XXX",
        "   ",
    ], T_COLOR),
]
