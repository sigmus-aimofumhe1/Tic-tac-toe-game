import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
winner = None
game_running = True

# Game board
def display_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

# Take a player input
def player_input(board):
    prompt = int(input("Choose a spot (1-9): "))
    if board[prompt - 1] == "-":
        board[prompt -1 ] = current_player
    else:
        print("Please, choose a valid spot (between 1 - 9).")

# Check for win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def check_if_win(board):
    global game_running
    if check_horizontal(board):
        display_board(board)
        print(f"The winner is {winner}!")
        game_running = False

    elif check_horizontal(board):
        display_board(board)
        print(f"The winner is {winner}!")
        game_running = False

    elif check_diagonal(board):
        display_board(board)
        print(f"The winner is {winner}!")
        game_running = False


def check_if_tie(board):
    global game_running
    if "-" not in board:
        display_board(board)
        print("It is a tie!")
        game_running = False


# switch player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()


while game_running:
    display_board(board)
    player_input(board)
    check_if_win(board)
    check_if_tie(board)
    switch_player()
    computer(board)
    check_if_win(board)
    check_if_tie(board)

