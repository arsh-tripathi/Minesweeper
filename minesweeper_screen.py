import tkinter as tk
import minesweeper_oop as mo

def run(size,difficulty):
    def flag(event):
        event.widget.configure(text="F")
    

    screen = tk.Tk()
    screen.title("Minesweeper")
    screen.geometry("1960x1680")
    button_grid = [[tk.Button(screen, width=2,height=1) for i in range(size)] for j in range(size)]

    game_board = mo.Board()
    game_board.setup_board(size,difficulty)


    def onclick(x,y):
        game_board.uncover(x,y)
        if (game_board.win_check()):
            tk.Label(screen, text="You win!",font=("Arial",30)).place(x=100,y=100)
            game_board.reset()
        for i in range(size):
            for j in range(size):
                result = game_board.tiles[i][j].face_value
                if (result == "B"):
                    button_grid[i][j].configure(text=result,relief="sunken")
                    tk.Label(screen, text="Game over!",font=("Arial",30)).place(x=100,y=100)
                    for x in range(size):
                        for y in range(size):
                            button_grid[x][y].destroy()
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

#run(11,7)
