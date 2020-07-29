# ------------ Global variables -----------
# Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_still_going = True
winner = None
current_player = "O"


# Display board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# Play
def play_game():
    print("\n")
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    # Fin del juego
    if winner == "X" or winner == "O":
        print(f"\nEl ganador es {winner}!")
    elif winner is None:
        print("Empate.")


# Handle turn
def handle_turn(player):

    print(f"Es turno de {player}")
    position = input("Elige una posición (1-9): ")

    while (position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]) or (board[int(position) - 1] != "-"):
        position = input("Entrada inválida. Elige una posición (1-9): ")

    position = int(position) - 1
    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


# Check Win
def check_for_winner():
    global winner

    # Check rows
    row_winner = check_rows()
    # Check columns
    column_winner = check_columns()
    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


# Check Tie
def check_if_tie():

    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


# Flip Player
def flip_player():

    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return


play_game()
