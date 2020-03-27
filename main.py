
# game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# if game still going
game_still_going = True

# who won or tie?
winner = None

# Who's turn is it
current_player = "X"


# display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# play game
def play_game():
    # display initial board
    display_board()

    while game_still_going:
        # handle a single turn
        handle_turn(current_player)
        # check if the game ended
        check_if_game_over()
        # flip to other player
        flip_player()
    # the game has ended
    if winner == "X" or winner == "O":
        print("Congrats " + winner + " you won.")
    elif winner == None:
        print("Tie.")


# handle turn of player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose position from 1-9: ")

    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid pick. Choose position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again")

    board[position] = player

    display_board()


# check if game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# check if win
def check_for_winner():

    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
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


# check rows
def check_rows():

    global game_still_going
    # check if any of the rows have the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


# check columns
def check_columns():
    global game_still_going
    # check if any of the rows have the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


# check diagonals
def check_diagonals():
    global game_still_going
    # check if any of the rows have the same value
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"

    # if
    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return


# check if tie
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


# flip player
def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()