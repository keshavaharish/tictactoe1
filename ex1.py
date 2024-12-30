import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
        
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def ai_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(empty_cells)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    user_symbol = 'X'
    ai_symbol = 'O'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row = int(input(f"Enter row (0-2) for {user_symbol}: "))
        col = int(input(f"Enter column (0-2) for {user_symbol}: "))
        if board[row][col] == ' ':
            board[row][col] = user_symbol
        else:
            print("Cell already taken. Try again.")
            continue

        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break

        
        row, col = ai_move(board)
        board[row][col] = ai_symbol
        print(f"AI plays at ({row}, {col})")
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break

        
        if all(board[r][c] != ' ' for r in range(3) for c in range(3)):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
