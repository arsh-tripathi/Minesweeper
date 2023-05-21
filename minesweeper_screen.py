import tkinter as tk
import minesweeper_oop as mo

flag_img = 0
def run(size,difficulty):
    global flag_img
    screen = tk.Tk()
    game_board = mo.Board()
    game_board.setup_board(size,difficulty)
    flag_img = tk.PhotoImage(master=screen,file="./images/flag.png")
    def flag(event):
        global flag_img
        event.widget.configure(image=flag_img, width=18, height=20)
        #event.widget.configure(text="F")
    
    screen.title("Minesweeper")
    screen.geometry("1600x1600")
    screen.configure(bg="#1B1F2F")
    button_grid = [[tk.Button(screen, width=2,height=1,fg="#00fae6", bg="#1B1F2F") for i in range(size)] for j in range(size)]


    def onclick(x,y):
        game_board.uncover(x,y)
        if (game_board.win_check()):
            tk.Label(screen, text="You win!",font=("Arial",30), fg="#00fae6", bg="#1B1F2F").place(x=100,y=100)
            for x in range(size):
                        for y in range(size):
                            button_grid[x][y].destroy()
        for i in range(size):
            for j in range(size):
                result = game_board.tiles[i][j].face_value
                if (result == "B"):
                    button_grid[i][j].configure(text=result,relief="sunken")
                    tk.Label(screen, text="Game over!",font=("Arial",30), fg="#00fae6", bg="#1B1F2F").place(x=100,y=100)
                    for x in range(size):
                        for y in range(size):
                            button_grid[x][y].destroy()
                elif (result == 1):
                    button_grid[i][j].configure(image='',text=result,relief="sunken",fg="yellow", width=2,height=1)
                elif (result == 2):
                    button_grid[i][j].configure(image='',text=result,relief="sunken",fg="orange", width=2,height=1)
                elif (result == 3):
                    button_grid[i][j].configure(image='',text=result,relief="sunken",fg="red", width=2,height=1)
                elif (result == 4):
                    button_grid[i][j].configure(image='',text=result,relief="sunken",fg="purple", width=2,height=1)
                elif (result == "@"):
                    button_grid[i][j].configure(image=flag_img)
                elif (result != "#"):
                    button_grid[i][j].configure(image='',text=result,relief="sunken",fg="green", width=2,height=1)

    for i in range(size):
        for j in range(size):
            button_grid[i][j].place(x=24*i,y=24*j)
            button_grid[i][j].configure(command=lambda x=i, y=j: onclick(x,y))
            button_grid[i][j].bind("<Button-2>", flag)
            button_grid[i][j].bind("<Button-3>", flag)


    screen.mainloop()

#run(11,7)
