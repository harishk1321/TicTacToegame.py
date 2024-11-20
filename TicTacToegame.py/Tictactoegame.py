import math

# Initialize the board
def initialize_board():
    return [' ' for _ in range(9)]

# Print the board
def print_board(board):
    print("\n")
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("| " + " | ".join(row) + " |")
    print("\n")

# Check for a winner
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]
    return None

# Check if the board is full (tie)
def is_board_full(board):
    return ' ' not in board

# Evaluate the board score for the AI
def evaluate(board):
    winner = check_winner(board)
    if winner == 'O':  # AI wins
        return 1
    elif winner == 'X':  # Human wins
        return -1
    return 0  # Tie or ongoing game

# Minimax algorithm with optional Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    score = evaluate(board)

    # Base case: game over or board full
    if score == 1 or score == -1 or is_board_full(board):
        return score

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

# Main game loop
def tic_tac_toe():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', and the AI is 'O'.")
    print_board(board)

    while True:
        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[move] = 'X'
        print_board(board)

        # Check for end game
        if check_winner(board) == 'X':
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        # AI move
        print("AI is making a move...")
        ai_move = find_best_move(board)
        board[ai_move] = 'O'
        print_board(board)

        # Check for end game
        if check_winner(board) == 'O':
            print("AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
