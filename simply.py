"""
Tic Tac Toe Game
"""
game_board = [[" ", "|", " ", "|", " "],
              ["-", "+", "-", "+", "-"],
              [" ", "|", " ", "|", " "],
              ["-", "+", "-", "+", "-"],
              [" ", "|", " ", "|", " "]]

def print_game_board(board):
    """game board

    Args:
        board (list): printing game board
    """
    for row in board:
        for column in row:
            print(column, end=' ')
        print()

position = int(input("Enter the position: "))

def position_on_bord(pos):
    """adding elements to list

    Args:
        pos (int): adding X or O to the board
    """
    if pos == 1:
        game_board[0][0] = 'X'
    elif pos == 2:
        game_board[0][2] = 'X'
    elif pos == 3:
        game_board[0][4] = 'X'
    elif pos == 4:
        game_board[2][0] = 'X'
    elif pos == 5:
        game_board[2][2] = 'X'
    elif pos == 6:
        game_board[2][4] = 'X'
    elif pos == 7:
        game_board[4][0] = 'X'
    elif pos == 8:
        game_board[4][2] = 'X'
    elif pos == 9:
        game_board[4][4] = 'X'

position_on_bord(position)
print_game_board(game_board)
