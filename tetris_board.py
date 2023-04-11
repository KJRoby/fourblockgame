# tetris_board.py
import tetris_constants

# Add Tetromino to the board
def add_to_board(board, tetromino):
    for row in range(len(tetromino.shape)):
        for col in range(len(tetromino.shape[row])):
            if tetromino.shape[row][col] == "X":
                board[tetromino.y + row][tetromino.x + col] = tetromino.color
    return board

# Remove complete lines
def remove_complete_lines(board):
    full_lines = [i for i, row in enumerate(board) if all(cell != " " for cell in row)]
    if full_lines:
        board = [row for i, row in enumerate(board) if i not in full_lines]
        for _ in range(len(full_lines)):
            board.insert(0, [" " for _ in range(tetris_constants.GRID_WIDTH)])
    return len(full_lines), board