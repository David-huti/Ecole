def display_board(board):
    """Display the game board."""
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()


def check_winner(board, player):
    """Check if the player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def play_game():
    """Run the TicTacToe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves = 0

    print("Welcome to TicTacToe!")
    print("Player X and Player O take turns.")
    print("Choose a row and a column between 1 and 3.")

    while moves < 9:
        display_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Choose a row (1-3): ")) - 1
            col = int(input("Choose a column (1-3): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position. Choose numbers between 1 and 3.")
            continue

        if board[row][col] != " ":
            print("This cell is already occupied. Try again.")
            continue

        board[row][col] = current_player
        moves += 1

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    display_board(board)
    print("It's a draw!")


play_game()
