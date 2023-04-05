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
        self.board[0][0]["text"] = "R"
        self.board[0][1]["text"] = "N"
        self.board[0][2]["text"] = "B"
        self.board[0][3]["text"] = "Q"
        self.board[0][4]["text"] = "K"
        self.board[0][5]["text"] = "B"
        self.board[0][6]["text"] = "N"
        self.board[0][7]["text"] = "R"
        for col in range(8):
            self.board[1][col]["text"] = "P"
            self.board[6][col]["text"] = "p"
        self.board[7][0]["text"] = "r"
        self.board[7][1]["text"] = "n"
        self.board[7][2]["text"] = "b"
        self.board[7][3]["text"] = "q"
        self.board[7][4]["text"] = "k"
        self.board[7][5]["text"] = "b"
        self.board[7][6]["text"] = "n"
        self.board[7][7]["text"] = "r"

        # Set up event handlers
        for row in range(8):
            for col in range(8):
                self.board[row][col]["command"] = lambda row=row, col=col: self.on_click(row, col)

        self.selected = None

    def on_click(self, row, col):
        if self.selected is None:
            self.selected = (row, col)
        else:
            # Move selected piece to new position
            piece = self.board[self.selected[0]][self.selected[1]]["text"]
            self.board[self.selected[0]][self.selected[1]]["text"] = ""
            self.board[row][col]["text"] = piece
            self.selected = None

if __name__ == "__main__":
    root = tk.Tk()
    game = ChessBoard(root)
    root.mainloop()
