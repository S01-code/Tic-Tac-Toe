#!/usr/bin/env python3
"""
Tic Tac Toe Game - Console Version
Clean and elegant console-based game for two players.

Design inspiration: Minimal, elegant style with clear typography and spacing
"""

import os

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the game header with elegant styling."""
    print("\n" + "=" * 33)
    print("    TIC TAC TOE  -  Two Players")
    print("=" * 33 + "\n")

def create_board():
    """Create an empty Tic Tac Toe board."""
    return [' '] * 9

def print_board(board):
    """Print the Tic Tac Toe board."""
    # Using box drawing characters for better visuals
    print("    1   2   3")
    print("  ┌───┬───┬───┐")
    for row in range(3):
        row_cells = []
        for col in range(3):
            row_cells.append(f" {board[row * 3 + col]} ")
        print(f"{row+1} │" + "│".join(row_cells) + "│")
        if row < 2:
            print("  ├───┼───┼───┤")
    print("  └───┴───┴───┘\n")

def is_winner(board, player):
    """Check if the specified player has won."""
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def is_board_full(board):
    """Check if the board is full (no empty spaces)."""
    return all(cell != ' ' for cell in board)

def get_player_move(board, player):
    """Prompt the player to make a move."""
    while True:
        try:
            move = input(f"Player {player} - Enter your move (row,col): ").strip()
            if move.lower() in ('q', 'quit', 'exit'):
                print("Exiting game. Goodbye!")
                exit(0)
            row_str, col_str = move.split(',')
            row = int(row_str) - 1
            col = int(col_str) - 1
            if row not in range(3) or col not in range(3):
                print("Invalid input. Rows and columns must be between 1 and 3.")
                continue
            idx = row * 3 + col
            if board[idx] != ' ':
                print("That cell is already taken. Please choose another.")
                continue
            return idx
        except ValueError:
            print("Invalid input format. Please enter row and column as two numbers separated by a comma, e.g., '2,3'.")
            continue

def play_game():
    """Main game logic."""
    board = create_board()
    current_player = 'X'

    clear_console()
    print_header()
    print_board(board)

    while True:
        idx = get_player_move(board, current_player)
        board[idx] = current_player

        clear_console()
        print_header()
        print_board(board)

        if is_winner(board, current_player):
            print(f"🎉 Player {current_player} wins! Congratulations! 🎉\n")
            break
        elif is_board_full(board):
            print("It's a tie! No more moves left.\n")
            break
        else:
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

    # Prompt to play again
    while True:
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again in ('y', 'yes'):
            play_game()
            return
        elif again in ('n', 'no'):
            print("Thanks for playing Tic Tac Toe. Goodbye!")
            return
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    play_game()

