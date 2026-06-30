# Tic Tac Toe with AI

A graphical Tic Tac Toe game developed in Python using Tkinter. This project features an intelligent AI opponent powered by the Minimax algorithm, along with a knowledge based hint system that suggests potential winning moves to the player.

## Features

- Interactive graphical user interface built with Tkinter
- Human vs AI gameplay
- Unbeatable AI using the Minimax algorithm
- Knowledge based hint system for winning move suggestions
- Automatic win and draw detection
- Automatic game reset after each round
- Clean and user friendly interface

## Technologies Used

- Python 3
- Tkinter
- Object Oriented Programming
- Minimax Algorithm
- Knowledge Based Reasoning

## How It Works

The player always plays as **X**, while the computer plays as **O**.

After each player move, the game:
1. Checks whether the player has won.
2. Detects if the game has ended in a draw.
3. Uses the Minimax algorithm to calculate the best possible move for the AI.
4. Displays the AI's move automatically.
5. Continues until either the player or the AI wins, or the game ends in a draw.

The project also includes a knowledge based hint feature that analyzes the current board and identifies potential winning moves for the player.

## Project Structure

```
tictactoe/
│
├── tic_tac_toe.py
├── README.md
└── .gitignore
```

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/tic-tac-toe-ai.git
```

Navigate to the project directory:

```bash
cd tic-tac-toe-ai
```

Run the game:

```bash
python tic_tac_toe.py
```

## Future Improvements

- Difficulty levels
- Highlight the winning line
- Scoreboard
- Player name customization
- Sound effects
- Dark mode
- Undo move functionality

## Learning Outcomes

This project helped strengthen my understanding of:

- Python programming
- GUI development using Tkinter
- Object Oriented Programming
- Event driven programming
- Artificial Intelligence through the Minimax algorithm
- Knowledge representation using dictionaries
- Game logic and state management

## Author

Sumaiya Morshed

Computer Science Graduate

Feel free to explore the project and share your feedback.
