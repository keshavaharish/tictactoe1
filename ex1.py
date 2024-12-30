import tkinter as tk
from tkinter import messagebox
import random

def check_winner(board):
    # Check rows, columns, and diagonals
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

def click(row, col):
    if board[row][col] == ' ' and not winner:
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state='disabled')
        update_game()

def update_game():
    global winner
    winner = check_winner(board)
    if winner:
        end_game(f"{winner} wins!")
        return
    if all(board[r][c] != ' ' for r in range(3) for c in range(3)):
        end_game("It's a draw!")
        return
    row, col = ai_move(board)
    board[row][col] = 'O'
    buttons[row][col].config(text='O', state='disabled')
    winner = check_winner(board)
    if winner:
        end_game(f"{winner} wins!")
    elif all(board[r][c] != ' ' for r in range(3) for c in range(3)):
        end_game("It's a draw!")

def end_game(message):
    messagebox.showinfo("Game Over", message)
    root.destroy()

# Initialize GUI
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize board and GUI elements
board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
winner = None

# Create buttons
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text='', font=('Arial', 24), height=2, width=5,
                                  command=lambda row=r, col=c: click(row, col))
        buttons[r][c].grid(row=r, column=c)

# Start the game loop
root.mainloop()
