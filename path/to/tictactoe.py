def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_win(board, player):
    """Checks if the player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def check_draw(board):
    """Checks if the game is a draw."""
    return all(cell != "" for row in board for cell in row)


def play_tictactoe():
    """Plays the Tic-Tac-Toe game."""
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, it's your turn.")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "":
            board[row][col] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch players
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    play_tictactoe()
