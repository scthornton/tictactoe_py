import random
import time


class TicTacToe:
    def __init__(self):
        # Initialize the 3x3 board with empty spaces
        # Think of this like setting up 9 empty tables in a restaurant
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # X always goes first
        self.game_mode = None  # Will be set during game setup
        self.human_player = 'X'  # Human is always X in single-player mode
        self.computer_player = 'O'  # Computer is always O in single-player mode

    def display_board(self):
        """Display the current state of the board"""
        print("\n   0   1   2")  # Column headers
        for i in range(3):
            print(
                f"{i}  {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} ")
            if i < 2:  # Don't print line after last row
                print("  ---|---|---")
        print()

    def make_move(self, row, col):
        """
        Place a move on the board
        Like a customer claiming a specific table in our restaurant
        Returns True if move was successful, False if spot taken
        """
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self):
        """
        Check if there's a winner
        Like checking if any customer has completed a full meal set
        """
        # Check rows - like checking horizontal lines of tables
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns - like checking vertical lines of tables
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Check diagonals - like checking corner-to-corner paths
        # Top-left to bottom-right diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]

        # Top-right to bottom-left diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None  # No winner yet

    def is_board_full(self):
        """
        Check if the board is completely filled
        Like checking if all restaurant tables are occupied
        """
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def get_empty_cells(self):
        """
        Get all empty cells on the board
        Like finding all available tables in the restaurant
        """
        empty_cells = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    empty_cells.append((row, col))
        return empty_cells

    def minimax(self, depth, is_maximizing):
        """
        Minimax algorithm for computer AI
        Think of it as the computer's strategic thinking process -
        like a chess master considering all possible future moves
        """
        winner = self.check_winner()

        # Base cases - game is over
        if winner == self.computer_player:
            return 10 - depth  # Computer wins (prefer faster wins)
        elif winner == self.human_player:
            return depth - 10  # Human wins (prefer slower losses)
        elif self.is_board_full():
            return 0  # Tie

        if is_maximizing:
            # Computer's turn - try to maximize score
            max_eval = float('-inf')
            for row, col in self.get_empty_cells():
                self.board[row][col] = self.computer_player
                eval_score = self.minimax(depth + 1, False)
                self.board[row][col] = ' '  # Undo move
                max_eval = max(max_eval, eval_score)
            return max_eval
        else:
            # Human's turn - try to minimize score (from computer's perspective)
            min_eval = float('inf')
            for row, col in self.get_empty_cells():
                self.board[row][col] = self.human_player
                eval_score = self.minimax(depth + 1, True)
                self.board[row][col] = ' '  # Undo move
                min_eval = min(min_eval, eval_score)
            return min_eval

    def get_best_computer_move(self):
        """
        Find the best move for the computer using minimax
        Like a master strategist calculating the optimal restaurant table choice
        """
        best_score = float('-inf')
        best_move = None

        for row, col in self.get_empty_cells():
            # Make temporary move
            self.board[row][col] = self.computer_player
            score = self.minimax(0, False)
            self.board[row][col] = ' '  # Undo move

            # Add small bonus for center and corners to break ties strategically
            if row == 1 and col == 1:  # Center
                score += 0.1
            elif (row, col) in [(0, 0), (0, 2), (2, 0), (2, 2)]:  # Corners
                score += 0.05

            if score > best_score:
                best_score = score
                best_move = (row, col)

        return best_move

    def make_computer_move(self):
        """
        Execute computer's move with some personality
        Like a confident chef choosing their signature dish
        """
        print("🤖 Computer is thinking...")
        time.sleep(1)  # Add suspense!

        move = self.get_best_computer_move()
        if move:
            row, col = move
            self.make_move(row, col)
            print(f"Computer chooses row {row}, column {col}")

    def switch_player(self):
        """
        Switch between X and O players
        Like alternating between two customers taking turns
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_valid_human_move(self):
        """
        Get a valid move from the human player
        Like taking an order and making sure the table is available
        """
        while True:
            try:
                print(f"Player {self.current_player}'s turn")
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))

                # Check if coordinates are within bounds
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid coordinates! Please enter numbers between 0 and 2.")
                    continue

                # Try to make the move
                if self.make_move(row, col):
                    return True
                else:
                    print("That spot is already taken! Choose another.")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

    def choose_game_mode(self):
        """
        Let the player choose between single-player and two-player modes
        Like asking if they want to dine alone or with a friend
        """
        while True:
            try:
                print("\n🎮 Welcome to Tic Tac Toe!")
                print("Choose your game mode:")
                print("1️⃣  Single Player (vs Computer)")
                print("2️⃣  Two Players (Human vs Human)")

                choice = int(input("\nEnter your choice (1 or 2): "))

                if choice == 1:
                    self.game_mode = "single"
                    print("\n🤖 You'll be playing against the computer!")
                    print("You are X, Computer is O. Good luck! 🍀")
                    return
                elif choice == 2:
                    self.game_mode = "two_player"
                    print("\n👥 Two-player mode selected!")
                    print("Player 1 is X, Player 2 is O")
                    return
                else:
                    print("Invalid choice! Please enter 1 or 2.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    def play_game(self):
        """
        Main game loop - orchestrates the entire game
        Like managing the entire restaurant operation
        """
        self.choose_game_mode()

        print("\nEnter coordinates as row (0-2) and column (0-2)")

        while True:
            # Show current board state
            self.display_board()

            # Handle different game modes
            if self.game_mode == "single":
                if self.current_player == self.human_player:
                    # Human's turn
                    self.get_valid_human_move()
                else:
                    # Computer's turn
                    self.make_computer_move()
            else:
                # Two-player mode - both are human
                self.get_valid_human_move()

            # Check if current player won
            winner = self.check_winner()
            if winner:
                self.display_board()
                if self.game_mode == "single":
                    if winner == self.human_player:
                        print("🎉 Congratulations! You beat the computer! 🎉")
                    else:
                        print("🤖 Computer wins! Better luck next time! 🤖")
                else:
                    print(f"🎉 Player {winner} wins! 🎉")
                break

            # Check if it's a tie
            if self.is_board_full():
                self.display_board()
                if self.game_mode == "single":
                    print("🤝 It's a tie! You played well against the computer!")
                else:
                    print("🤝 It's a tie! Good game!")
                break

            # Switch to the other player
            self.switch_player()


# Create and start a new game
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()

    # Ask if they want to play again
    while input("\nPlay again? (y/n): ").lower().startswith('y'):
        game = TicTacToe()  # Create fresh game
        game.play_game()
