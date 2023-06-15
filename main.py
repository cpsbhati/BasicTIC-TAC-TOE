# Tic-Tac-Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if there is a winner
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to play the game
def play_game():
    player = 'X'
    while True:
        print_board()
        position = int(input("Enter a position (1-9): ")) - 1

        if board[position] == ' ':
            board[position] = player
        else:
            print("Invalid move. Try again.")
            continue

        if check_winner(board, player):
            print_board()
            print("Player", player, "wins!")
            break

        if ' ' not in board:
            print_board()
            print("It's a tie!")
            break

        player = 'O' if player == 'X' else 'X'

# Start the game
play_game()
