import tkinter as tk
from random import randint

main_screen = tk.Tk()
size = 11
mine_count = 8
grid = []
uncovered_locations = []


def set_mines():
    global grid
    global mine_count
    x_list = []
    y_list = []
    i = 0
    while i < mine_count:
        x = randint(0, size-1)
        while x in x_list:
            x = randint(0, size-1)
        x_list.append(x)
        y = randint(0, size-1)
        while y in y_list:
            y = randint(0, size-1)
        y_list.append(y)
        i = i + 1
    return list(zip(x_list, y_list))


def neighbour_bomb_count(x, y, mines):
    neighbours = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y),
                  (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
    count = 0
    i = 0
    while i < 8:
        if neighbours[i] in mines:
            count = count + 1
        else:
            pass
        i = i+1
    return count


def update_numbers(mines):
    global size
    global grid
    ls = []
    x = 0
    while x < size:
        y = 0
        while y < size:
            if (x, y) in mines:
                ls.append('B')
                y = y + 1
            else:
                ls.append(neighbour_bomb_count(x, y, mines))
                y = y + 1
        x = x + 1
    i = 0
    while i < size*size:
        j = 0
        row = []
        while j < size:
            row.append(ls[i+j])
            j = j + 1
        grid.append(row)
        i = i+size


def button_grid():
    global size
    global grid
    i = 0
    while i < size:
        j = 0
        while j < size:
            tk.Button(text=grid[i][j], height=1,
                      width=2, relief="sunken").place(x=i*25, y=j*25)
            j = j + 1
        i = i + 1


def uncover_zero_neighbours(b, x, y):
    global uncovered_locations
    neighbours = [[x-1, y-1], [x, y-1], [x+1, y-1], [x-1, y],
                  [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]]
    if x == size - 1:
        neighbours.remove([x+1, y-1])
        neighbours.remove([x+1, y])
        neighbours.remove([x+1, y+1])
    elif x == 0:
        neighbours.remove([x-1, y-1])
        neighbours.remove([x-1, y])
        neighbours.remove([x-1, y+1])
    if y == size - 1:
        neighbours.remove([x-1, y+1])
        neighbours.remove([x, y+1])
        neighbours.remove([x+1, y+1])
    elif y == 0:
        neighbours.remove([x-1, y-1])
        neighbours.remove([x-1, y])
        neighbours.remove([x-1, y+1])
    b.destroy()
    i = 0
    length = len(neighbours)
    while i < length:
        if neighbours[i] in uncovered_locations:
            i = i + 1
        else:
            uncover(b, neighbours[i][0], neighbours[i][1])
            i = i + 1


def uncover(b, i, j):
    global grid
    global uncovered_locations
    if i < 0 or j < 0 or i >= size or j >= size:
        pass
    if grid[i][j] == 'B':
        tk.Label(text="Game Over", font=("Arial", 30)).place(x=30, y=30)
    elif grid[i][j] == 0:
        uncovered_locations.append([i, j])
        uncover_zero_neighbours(b, i, j)
    else:
        b.destroy()
        uncovered_locations.append([i, j])


def cover_grid():
    global size
    global grid
    button = [[0]*size]*size
    i = 0
    while i < size:
        j = 0
        while j < size:
            button[i][j] = tk.Button(height=1, width=2)
            button[i][j].place(x=i*25, y=j*25)
            button[i][j].configure(
                command=lambda b=button[i][j], x=i, y=j: uncover(b, x, y))

            j = j + 1
        i = i + 1


update_numbers(set_mines())
button_grid()
cover_grid()

main_screen.mainloop()
