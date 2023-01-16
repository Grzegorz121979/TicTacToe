"""
Tic Tac Toe Game
"""
game_board = [[" ", "|", " ", "|", " "],
              ["-", "+", "-", "+", "-"],
              [" ", "|", " ", "|", " "],
              ["-", "+", "-", "+", "-"],
              [" ", "|", " ", "|", " "]]

player_position = []
computer_position = []

def print_game_board(board):
    """game board

    Args:
        board (list): printing game board
    """
    for row in board:
        for column in row:
            print(column, end=' ')
        print()

def position_on_bord(board, pos, user):
    """_summary_

    Args:
        pos (_int_): _description_
        user (_string_): _description_
    """
    if user == "player":
        symbol = 'X'
        player_position.append(pos)
    elif user == "cpu":
        symbol = 'O'
        computer_position.append(pos)
    
    if pos == 1:
        board[0][0] = symbol
    elif pos == 2:
        board[0][2] = symbol
    elif pos == 3:
        board[0][4] = symbol
    elif pos == 4:
        board[2][0] = symbol
    elif pos == 5:
        board[2][2] = symbol
    elif pos == 6:
        board[2][4] = symbol
    elif pos == 7:
        board[4][0] = symbol
    elif pos == 8:
        board[4][2] = symbol
    elif pos == 9:
        board[4][4] = symbol        
   
position = int(input("Enter the position: "))
position_on_bord(game_board, position, user="player")
print_game_board(game_board)
