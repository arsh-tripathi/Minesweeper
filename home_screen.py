import tkinter as tk
import minesweeper_screen as ms

difficulty_level = 0
size = 0

def play_game():
    ms.run(size,difficulty_level) 

home_screen = tk.Tk()
home_screen.title("Minesweeper")
home_screen.configure(bg="#1B1F2F")
play = tk.Button(text="Play",command=play_game, font=("Cascadia Code", 9), fg="#00fae6", bg="#1B1F2F")
difficulty_label = tk.Label(text="Difficulty: ", font=("Cascadia Code", 9), fg="#00fae6", bg="#1B1F2F")

def select_size(value):
    global size
    global difficulty_level
    size = value
    difficulty_level = (size - 5) * 3
    if (value == 9):
        difficulty_label.configure(text="Small game selected")
    elif (value == 18):
        difficulty_label.configure(text="Medium game selected")
    elif (value == 25):
        difficulty_label.configure(text="Huge game selected")
    difficulty_label.pack(pady=20)
    play.pack(pady=20)

welcome_label = tk.Label(text="Minesweeper Recreated", font=("Cascadia Code", 35), fg="#00fae6", bg="#1B1F2F").pack()
select_difficulty_label = tk.Label(text="Select the game size", font=("Cascadia Code", 20), fg="#00fae6", bg="#1B1F2F").pack(pady=30)
easy_difficulty = tk.Button(text="Small", font=("Cascadia Code", 9), fg="#00fae6", bg="#1B1F2F", activebackground="white")
easy_difficulty.configure(command=lambda: select_size(9))
medium_difficulty = tk.Button(text="Medium", font=("Cascadia Code", 9), fg="#00fae6", bg="#1B1F2F")
medium_difficulty.configure(command=lambda: select_size(18))
hard_difficulty = tk.Button(text="Huge", font=("Cascadia Code", 9), fg="#00fae6", bg="#1B1F2F")
hard_difficulty.configure(command=lambda: select_size(25))
easy_difficulty.pack(pady=5)
medium_difficulty.pack(pady=5)
hard_difficulty.pack(pady=5)





home_screen.mainloop()
