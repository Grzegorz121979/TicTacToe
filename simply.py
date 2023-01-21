"""
Tic Tac Toe Game
"""
import random
import collections
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
        pos (int): _description_
        user (string): _description_
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

def victory_conditions():
    """function
    """
    victory_positions = []
    top_row = [1, 2, 3]
    mid_row = [4, 5, 6]
    bot_row = [7, 8, 9]
    left_col = [1, 4, 7]
    mid_col = [2, 5, 8]
    right_col = [3, 6, 9]
    left_cross = [1, 5, 9]
    right_cross = [3, 5, 7]
    victory_positions.append(top_row)
    victory_positions.append(mid_row)
    victory_positions.append(bot_row)
    victory_positions.append(left_col)
    victory_positions.append(mid_col)
    victory_positions.append(right_col)
    victory_positions.append(left_cross)
    victory_positions.append(right_cross)
    for index, value in enumerate(victory_positions):
        if collections.Counter(player_position) >= collections.Counter(value):
            return "YOU WIN!!!"
        if collections.Counter(computer_position) >= collections.Counter(value):
            return "Cpu win!"
        if len(player_position) + len(computer_position) == 9:
            return "Draw"
    return ""
print_game_board(game_board)
while True:
    player_numer = int(input("Enter the position: "))
    cpu_number = random.randint(1, 9)
    while player_numer in player_position or player_numer in computer_position:
        print("The position is taken: ")
        player_numer = int(input("Enter the position: "))
    position_on_bord(game_board, player_numer, user="player")
    print_game_board(game_board)
    print()
    print("---------")
    print()
    RESULT = victory_conditions()
    if len(RESULT) > 0:
        print(RESULT)
        break
    while cpu_number in computer_position or cpu_number in player_position:
        cpu_number = random.randint(1, 9)
    position_on_bord(game_board, cpu_number, user="cpu")
    RESULT = victory_conditions()
    print_game_board(game_board)
    if len(RESULT) > 0:
        print(RESULT)
        break
    