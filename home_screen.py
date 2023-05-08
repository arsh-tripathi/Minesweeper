import tkinter as tk
import minesweeper_screen as ms

difficulty_level = 0
size = 0

home_screen = tk.Tk()
def select_size(b, value):
    global size
    global difficulty_level
    size = value
    difficulty_level = (size - 5) * 3

welcome_label = tk.Label(text="Welcome to Minesweeper Recreated", font=("Arial", 45)).pack()
select_difficulty_label = tk.Label(text="Select the difficulty level", font=("Arial", 45)).pack()
easy_difficulty = tk.Button(text="Easy")
easy_difficulty.configure(command=lambda b=easy_difficulty: select_size(b,9))
medium_difficulty = tk.Button(text="Medium")
medium_difficulty.configure(command=lambda b=medium_difficulty: select_size(b,18))
hard_difficulty = tk.Button(text="Hard")
hard_difficulty.configure(command=lambda b=hard_difficulty: select_size(b,25))
easy_difficulty.pack()
medium_difficulty.pack()
hard_difficulty.pack()


def play_game():
    
    ms.run(size,difficulty_level) 

play = tk.Button(text="Play",command=play_game).pack()


home_screen.mainloop()
