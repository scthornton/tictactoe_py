class TicTacToe:
    def __init__(self):
        # Initialize the 3x3 board with empty spaces
        # Think of this like setting up 9 empty tables in a restaurant
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # X always goes first

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

    def switch_player(self):
        """
        Switch between X and O players
        Like alternating between two customers taking turns
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_valid_move(self):
        """
        Get a valid move from the current player
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

    def play_game(self):
        """
        Main game loop - orchestrates the entire game
        Like managing the entire restaurant operation
        """
        print("Welcome to Tic Tac Toe!")
        print("Players will take turns placing X's and O's")
        print("Enter coordinates as row (0-2) and column (0-2)")

        while True:
            # Show current board state
            self.display_board()

            # Get player's move
            self.get_valid_move()

            # Check if current player won
            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"🎉 Player {winner} wins! 🎉")
                break

            # Check if it's a tie
            if self.is_board_full():
                self.display_board()
                print("It's a tie! Good game!")
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
0
