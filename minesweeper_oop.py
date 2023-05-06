import tkinter as tk
from random import randint

class Tile():
    x = 0
    y = 0
    status = 0  # 0 means it is still covered
    display_value = 0
    is_bomb = False
    def set_coordinates(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def set_bomb(self):
        self.is_bomb = True
        self.display_value = "B"
    def increment_dis_val(self):
        self.display_value += 1
    def uncover(self):
        self.status = 1
    def print_object(self):
        print(self.display_value)
        #print("(x, y): (" + str(self.x) + "," + str(self.y) + ")")
        #print("status: " + str(self.status))
        #print("display_val: " + str(self.display_value))

def create_tile():
    return Tile()

class Board():
    size = 9
    status = 0 # 0 for active, 1 for completed, 2 for bomb pressed
    difficulty = 7
    uncovered = 0
    tiles = [[Tile() for i in range(9)] for j in range(9)]
    mine_locations = [[0 for i in range(2)] for i in range(difficulty)]
    mine_neighbours = []
    def modify_size(self, new_size):
        self.size = new_size
        self.tiles = [[Tile() for i in range(new_size)] for j in range(new_size)]
    def modify_difficulty(self, new_difficulty):
        self.mine_locations = [[0 for i in range(2)] for j in range(new_difficulty)]
    def update_coords(self):
        for i in range(self.size):
            for j in range(self.size):
                self.tiles[i][j].set_coordinates(i,j)
    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                #self.tiles[i][j].print_object()
                print(str(self.tiles[i][j].display_value) + " ", end="")
            print("")
    def set_mines(self):
        for i in range(self.difficulty):
            x = randint(0,self.size - 1)
            y = randint(0,self.size - 1)
            self.mine_locations[i][0] = x
            self.mine_locations[i][1] = y
            self.tiles[x][y].set_bomb()
            self.mine_neighbours.append([x-1,y-1])
            self.mine_neighbours.append([x,y-1])
            self.mine_neighbours.append([x+1,y-1])
            self.mine_neighbours.append([x-1,y])
            self.mine_neighbours.append([x+1,y])
            self.mine_neighbours.append([x-1,y+1])
            self.mine_neighbours.append([x,y+1])
            self.mine_neighbours.append([x+1,y+1])
    def update_neighbours(self):
        for coords in self.mine_neighbours:
            if ((coords[0] < self.size) and (coords[0] >= 0) and (coords[1] < self.size) and (coords[1] >= 0)
                and (self.tiles[coords[0]][coords[1]].display_value != "B")):
                self.tiles[coords[0]][coords[1]].increment_dis_val()

new_board = Board()
new_board.modify_size(11)
new_board.update_coords()
new_board.set_mines()
new_board.update_neighbours()
new_board.print_board()
