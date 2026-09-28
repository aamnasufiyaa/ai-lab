# Tic-Tac-Toe Game

board = [" " for _ in range(9)]

def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


current_player = "X"

for turn in range(9):
    display_board()

    print("Player", current_player)
    position = int(input("Enter position (1-9): ")) - 1

    if position < 0 or position > 8:
        print("Invalid position!")
        continue

    if board[position] != " ":
        print("Position already taken!")
        continue

    board[position] = current_player

    if check_winner(current_player):
        display_board()
        print("Player", current_player, "wins!")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

else:
    display_board()
    print("It's a draw!")
