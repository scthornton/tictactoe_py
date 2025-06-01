# 🎮 Tic Tac Toe

<div align="center">

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

*A modern, clean implementation of the classic Tic Tac Toe game in Python*

[Quick Start](#-quick-start) • [Features](#-features) • [How to Play](#-how-to-play) • [Code Structure](#-code-structure)

</div>

---

## ✨ Features

- 🎯 **Clean Terminal Interface** - Beautiful ASCII art board display
- 🤖 **Unbeatable AI Opponent** - Uses minimax algorithm for perfect play
- 🎮 **Multiple Game Modes** - Single-player vs AI or two-player human vs human
- 🛡️ **Robust Input Validation** - Handles all edge cases gracefully  
- 🔄 **Smart Turn Management** - Seamless player switching
- 🏆 **Win Detection** - Checks rows, columns, and diagonals
- 🧠 **Strategic AI** - Computer prefers center, blocks wins, and plays optimally
- 🎪 **Replay System** - Play multiple rounds without restarting
- 📱 **Cross-Platform** - Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation & Run
```bash
# Clone or download the tictactoe.py file
python tictactoe.py
```

That's it! No dependencies, no setup, just pure Python fun! 🐍

## 🎯 How to Play

### Game Mode Selection
When you start the game, choose your preferred mode:
- **1️⃣ Single Player** - Challenge the unbeatable AI computer
- **2️⃣ Two Players** - Classic human vs human gameplay

### Board Navigation
The game uses a **coordinate system** for easy navigation:

```
   0   1   2
0    |   |   
  ---|---|---
1    |   |   
  ---|---|---
2    |   |   
```

### Game Flow
1. **Player X** always goes first 🅰️
2. Enter your move as **row** then **column** (both 0-2)
3. Players alternate turns automatically
4. First to get **3 in a row** wins! 🏆
5. If all 9 spaces fill up, it's a tie 🤝

### AI Difficulty
The computer AI is **unbeatable** when playing optimally! It uses the minimax algorithm to:
- 🚫 Block all your winning moves
- ✅ Take winning opportunities immediately  
- 🎯 Play optimal opening strategy (prefers center)
- 🧠 Think several moves ahead

**Challenge Level:** The best you can achieve against the AI is a tie! 🤝

### Example Game Session
```
🎮 Welcome to Tic Tac Toe!
Choose your game mode:
1️⃣  Single Player (vs Computer)
2️⃣  Two Players (Human vs Human)

Enter your choice (1 or 2): 1

🤖 You'll be playing against the computer!
You are X, Computer is O. Good luck! 🍀

Player X's turn
Enter row (0-2): 1
Enter column (0-2): 1

   0   1   2
0    |   |   
  ---|---|---
1    | X |   
  ---|---|---
2    |   |   

🤖 Computer is thinking...
Computer chooses row 0, column 0

   0   1   2
0  O |   |   
  ---|---|---
1    | X |   
  ---|---|---
2    |   |   
```

## 🏗️ Code Structure

The game is built with **clean, object-oriented design**:

```python
class TicTacToe:
    ├── __init__()              # Initialize game state
    ├── display_board()         # Render the game board
    ├── make_move()             # Process player moves
    ├── check_winner()          # Detect win conditions
    ├── is_board_full()         # Check for ties
    ├── get_empty_cells()       # Find available moves
    ├── minimax()               # AI decision-making algorithm
    ├── get_best_computer_move() # Find optimal AI move
    ├── make_computer_move()    # Execute computer's turn
    ├── switch_player()         # Toggle between X and O
    ├── get_valid_human_move()  # Handle user input
    ├── choose_game_mode()      # Select single/two-player
    └── play_game()             # Main game loop
```

### Key Design Principles
- 🧩 **Modular Functions** - Each method has one clear responsibility
- 🤖 **Advanced AI** - Minimax algorithm with depth-aware scoring
- 🛡️ **Error Handling** - Graceful handling of invalid inputs
- 🎨 **Clean Interface** - Intuitive coordinate system
- 🔄 **State Management** - Reliable game state tracking

### AI Algorithm Details
The computer uses the **Minimax Algorithm** with these enhancements:
- **Depth-aware scoring** - Prefers faster wins and slower losses
- **Strategic positioning** - Prioritizes center, then corners, then edges
- **Perfect play** - Never makes suboptimal moves
- **Lookahead** - Considers all possible future game states

## 🎨 Game Preview

```
🎮 Welcome to Tic Tac Toe!
Choose your game mode:
1️⃣  Single Player (vs Computer)
2️⃣  Two Players (Human vs Human)

Enter your choice (1 or 2): 1

🤖 You'll be playing against the computer!
You are X, Computer is O. Good luck! 🍀

   0   1   2
0  X | O | X 
  ---|---|---
1  O | X | O 
  ---|---|---
2  X | O | X 

🤝 It's a tie! You played well against the computer!

Play again? (y/n): 
```

## 🛠️ Customization Ideas

Want to make it your own? Try adding:

- 🎨 **Colorized output** with `colorama`
- 🎵 **Sound effects** with `pygame`
- 🌐 **Web interface** with Flask
- 📱 **GUI version** with tkinter
- 📊 **Score tracking** across multiple games
- 🎚️ **Difficulty levels** (Easy AI that makes occasional mistakes)
- 🤖 **Different AI personalities** (Aggressive, Defensive, Random)
- 🎯 **Larger boards** (4x4, 5x5 with 4-in-a-row to win)
- 👥 **Network multiplayer** for online play
- 📈 **Game statistics** and win/loss tracking

## 🤝 Contributing

This is a learning project! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features  
- 🔧 Submit improvements
- ⭐ Star if you found it helpful!

## 📄 License

MIT License - feel free to use this code for learning, teaching, or building upon!

---

<div align="center">

**Made with ❤️ and Python**

*Happy Gaming! 🎮*

</div>