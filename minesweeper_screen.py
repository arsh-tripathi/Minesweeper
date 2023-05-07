import tkinter as tk
import minesweeper_oop as ms

def flag(event):
    event.widget.configure(text="F")

screen = tk.Tk("Minwsweeper")
screen.resizable()
screen.geometry("1960x1680")
size = 11    
button_grid = [[tk.Button(width=2,height=1) for i in range(size)] for j in range(size)]

game_board = ms.Board()
game_board.setup_board(11,7)


def onclick(x,y):
    game_board.uncover(x,y)
    if (game_board.win_check()):
        tk.Label(text="You win!",font=("Arial",30)).place(x=100,y=100)
    for i in range(size):
        for j in range(size):
            result = game_board.tiles[i][j].face_value
            if (result == "B"):
                button_grid[i][j].configure(text=result,relief="sunken")
                tk.Label(text="Game over!",font=("Arial",30)).place(x=100,y=100)
            elif (result == 1):
                button_grid[i][j].configure(text=result,relief="sunken",fg="blue")
            elif (result == 2):
                button_grid[i][j].configure(text=result,relief="sunken",fg="orange")
            elif (result == 3):
                button_grid[i][j].configure(text=result,relief="sunken",fg="red")
            elif (result == 4):
                button_grid[i][j].configure(text=result,relief="sunken",fg="purple")
            elif (result != "#"):
                button_grid[i][j].configure(text=result,relief="sunken",fg="green")

for i in range(size):
    for j in range(size):
        button_grid[i][j].place(x=24*i,y=24*j)
        button_grid[i][j].configure(command=lambda x=i, y=j: onclick(x,y))
        button_grid[i][j].bind("<Button-2>", flag)
        button_grid[i][j].bind("<Button-3>", flag)


screen.mainloop()