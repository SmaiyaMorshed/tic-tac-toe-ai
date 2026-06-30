import tkinter as tk
from tkinter import messagebox
import math

knowledge_base = {
    'Occupied': {}, 
    'Empty': {f'P{i}': True for i in range(1, 10)},
}

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Tic-Tac-Toe with AI")
        self.buttons = {}
        self.create_board()
        self.turn = 'X'

    def create_board(self):
        for idx in range(1, 10):
            row, col = divmod(idx - 1, 3)
            button = tk.Button(self.root, text='', font='Arial 20 bold', width=10, height=5,
                               command=lambda idx=idx: self.make_move(idx))
            button.grid(row=row, column=col)
            self.buttons[f'P{idx}'] = button

    def make_move(self, position):

        if self.turn != "X":
            return

        pos = f"P{position}"

        if knowledge_base["Empty"][pos]:

            self.buttons[pos].config(text="X")

            knowledge_base["Occupied"][pos] = "X"
            knowledge_base["Empty"][pos] = False

            if self.check_player_winner("X"):
                messagebox.showinfo("Game Over", "You win!")
                self.reset_game()
                return

            if all(not knowledge_base["Empty"][p] for p in knowledge_base["Empty"]):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
                return

            self.turn = "O"

            self.root.after(300, self.ai_move)

    def check_winning_move(self):
        winning_lines = [
            ["P1", "P2", "P3"],
            ["P4", "P5", "P6"],
            ["P7", "P8", "P9"],
            ["P1", "P4", "P7"],
            ["P2", "P5", "P8"],
            ["P3", "P6", "P9"],
            ["P1", "P5", "P9"],
            ["P3", "P5", "P7"]
        ]

        for line in winning_lines:
            x_count = sum(knowledge_base['Occupied'].get(pos) == 'X' for pos in line)
            empty_positions = [pos for pos in line if knowledge_base['Empty'].get(pos)]
            
            if x_count == 2 and len(empty_positions) == 1:
                return empty_positions[0]
        return None
    
    def check_player_winner(self, player):
        winning_lines = [
        ["P1","P2","P3"],
        ["P4","P5","P6"],
        ["P7","P8","P9"],
        ["P1","P4","P7"],
        ["P2","P5","P8"],
        ["P3","P6","P9"],
        ["P1","P5","P9"],
        ["P3","P5","P7"]
        ]

        for line in winning_lines:
            if all(knowledge_base["Occupied"].get(pos) == player for pos in line):
                return True

        return False

    def check_winner(self):
        winning_lines = [
            ["P1", "P2", "P3"],
            ["P4", "P5", "P6"],
            ["P7", "P8", "P9"],
            ["P1", "P4", "P7"],
            ["P2", "P5", "P8"],
            ["P3", "P6", "P9"],
            ["P1", "P5", "P9"],
            ["P3", "P5", "P7"]
        ]
        
        for line in winning_lines:
            if all(knowledge_base['Occupied'].get(pos) == self.turn for pos in line):
                return True
        return False

    def reset_game(self):
        for pos in self.buttons:
            self.buttons[pos].config(text='')
            knowledge_base['Empty'][pos] = True
        knowledge_base['Occupied'] = {}
        self.turn = 'X'

    def minimax(self, is_maximizing):

        if self.check_player_winner("O"):
            return 1

        if self.check_player_winner("X"):
            return -1

        if all(not knowledge_base["Empty"][p] for p in knowledge_base["Empty"]):
            return 0

        if is_maximizing:

            best = -math.inf

            for pos in knowledge_base["Empty"]:

                if knowledge_base["Empty"][pos]:

                    knowledge_base["Empty"][pos] = False
                    knowledge_base["Occupied"][pos] = "O"

                    score = self.minimax(False)

                    knowledge_base["Empty"][pos] = True
                    del knowledge_base["Occupied"][pos]

                    best = max(best, score)

            return best

        else:

            best = math.inf

            for pos in knowledge_base["Empty"]:

                if knowledge_base["Empty"][pos]:

                    knowledge_base["Empty"][pos] = False
                    knowledge_base["Occupied"][pos] = "X"

                    score = self.minimax(True)

                    knowledge_base["Empty"][pos] = True
                    del knowledge_base["Occupied"][pos]

                    best = min(best, score)

            return best

    def ai_move(self):

        best_score = -math.inf
        best_move = None

        for pos in knowledge_base["Empty"]:

            if knowledge_base["Empty"][pos]:

                knowledge_base["Empty"][pos] = False
                knowledge_base["Occupied"][pos] = "O"

                score = self.minimax(False)

                knowledge_base["Empty"][pos] = True
                del knowledge_base["Occupied"][pos]

                if score > best_score:
                    best_score = score
                    best_move = pos

        if best_move:

            knowledge_base["Empty"][best_move] = False
            knowledge_base["Occupied"][best_move] = "O"

            self.buttons[best_move].config(text="O")

            if self.check_player_winner("O"):
                messagebox.showinfo("Game Over", "AI wins!")
                self.reset_game()

            elif all(not knowledge_base["Empty"][p] for p in knowledge_base["Empty"]):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()

            else:
                self.turn = "X"
root = tk.Tk()
game = TicTacToeGame(root)
root.mainloop()
