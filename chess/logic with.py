import tkinter as tk

class ChessBoard:
    def __init__(self, master):
        self.master = master
        self.master.title("Chess Game")

        # Create 8x8 grid of buttons
        self.board = [[None for _ in range(8)] for _ in range(8)]
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                self.board[row][col] = tk.Button(master, width=5, height=2, bg=color)
                self.board[row][col].grid(row=row, column=col)

        # Set up initial chess positions
        self.pieces = {
            (0, 0): "R",
            (0, 1): "N",
            (0, 2): "B",
            (0, 3): "Q",
            (0, 4): "K",
            (0, 5): "B",
            (0, 6): "N",
            (0, 7): "R",
            (1, col): "P" for col in range(8),
            (6, col): "p" for col in range(8),
            (7, 0): "r",
            (7, 1): "n",
            (7, 2): "b",
            (7, 3): "q",
            (7, 4): "k",
            (7, 5): "b",
            (7, 6): "n",
            (7, 7): "r",
        }
        self.selected = None
        self.turn = "white"
        self.checkmate = False
        self.winner = None

        # Set up event handlers
        for row in range(8):
            for col in range(8):
                self.board[row][col]["command"] = lambda row=row, col=col: self.on_click(row, col)

    def on_click(self, row, col):
        if self.checkmate:
            return

        if self.selected is None:
            piece = self.pieces.get((row, col))
            if piece is not None and piece[0] == self.turn[0]:
                self.selected = (row, col)
        else:
            piece = self.pieces.get(self.selected)
            if (row, col) in self.get_valid_moves(piece, self.selected):
                # Move selected piece to new position
                self.pieces[self.selected] = None
                self.pieces[(row, col)] = piece
                self.board[self.selected[0]][self.selected[1]]["text"] = ""
                self.board[row][col]["text"] = piece
                self.selected = None

                # Check for checkmate
                if self.is_checkmate():
                    self.checkmate = True
                    self.winner = "black" if self.turn == "white" else "white"
                    tk.messagebox.showinfo("Game Over", f"{self.winner.capitalize()} wins!")
                else:
                    # Switch turns
                    self.turn = "black" if self.turn == "white" else "white"

        # Highlight valid moves for selected piece
        if self.selected is not None:
            piece = self.pieces.get(self.selected)
            if piece is not None:
                for row, col in self.get_valid_moves(piece, self.selected):
                    self.board[row][col]["bg"] = "light green"
        else:
            for row in range
