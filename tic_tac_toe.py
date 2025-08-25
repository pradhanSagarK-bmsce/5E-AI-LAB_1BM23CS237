import math

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check for winner
def check_winner(board):
    # Rows and Columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

# Check if board is full
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":  # AI wins
        return 1
    elif winner == "X":  # Player wins
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = "O"

# Convert cell number 1-9 to (row, col)
def cell_to_coords(cell):
    cell -= 1  # zero-based index
    return (cell // 3, cell % 3)

# Main Game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, Computer is O")
    print_board(board)

    while True:
        try:
            cell = int(input("Enter cell number (1-9): "))
            if cell < 1 or cell > 9:
                print("Invalid input! Enter a number between 1 and 9.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        row, col = cell_to_coords(cell)

        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue

        board[row][col] = "X"
        print_board(board)

        if check_winner(board) == "X":
            print("🎉 You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        ai_move(board)
        print("Computer played:")
        print_board(board)

        if check_winner(board) == "O":
            print("💻 Computer wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
