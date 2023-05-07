from random import randint

class Tile():
    x = 0
    y = 0
    status = 0  # 0 means it is still covered
    face_value = "#"
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
        self.face_value = self.display_value
    def flag(self):
        self.face_value = "@"
    def print_object(self):
        print(self.face_value)
        #print("(x, y): (" + str(self.x) + "," + str(self.y) + ")")
        #print("status: " + str(self.status))
        #print("display_val: " + str(self.display_value))

class Board():
    size = 9
    status = 0 # 0 for active, 1 for completed, 2 for bomb pressed
    difficulty = 7
    uncovered_count = 0
    uncovered = []
    non_bomb_location_count = 74
    tiles = [[Tile() for i in range(9)] for j in range(9)]
    mine_locations = [[0 for i in range(2)] for i in range(difficulty)]
    mine_neighbours = []
    def modify_size(self, new_size):
        self.size = new_size
        self.tiles = [[Tile() for i in range(new_size)] for j in range(new_size)]
        self.non_bomb_location_count = new_size * new_size - self.difficulty
    def modify_difficulty(self, new_difficulty):
        self.mine_locations = [[0 for i in range(2)] for j in range(new_difficulty)]
        self.non_bomb_location_count = self.size * self.size - new_difficulty
    def update_coords(self):
        for i in range(self.size):
            for j in range(self.size):
                self.tiles[i][j].set_coordinates(i,j)
    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                #self.tiles[i][j].print_object()
                print(str(self.tiles[i][j].face_value) + "  ", end="")
            print("")
    def set_mines(self):
        for i in range(self.difficulty):
            x = randint(0,self.size - 1)
            y = randint(0,self.size - 1)
            while ([x,y] in self.mine_locations):
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
    def setup_board(self, new_size, new_difficulty):
        self.modify_size(new_size)
        self.modify_difficulty(new_difficulty)
        self.update_coords()
        self.set_mines()
        self.update_neighbours()
    def uncover(self, x, y):
        coords = [x,y]
        if ((coords[0] < self.size) and (coords[0] >= 0) and (coords[1] < self.size) and (coords[1] >= 0)
            and (not(coords in self.uncovered))):
            if coords in self.mine_neighbours:
                self.tiles[x][y].uncover()
                self.uncovered.append(coords)
            elif coords in self.mine_locations:
                self.tiles[x][y].uncover()
                self.uncovered.append(coords)
                self.status = 2
            else:
                self.tiles[x][y].uncover()
                self.uncovered.append(coords)
                self.uncover(x-1,y-1)
                self.uncover(x-1,y)
                self.uncover(x-1,y+1)
                self.uncover(x,y-1)
                self.uncover(x,y+1)
                self.uncover(x+1,y-1)
                self.uncover(x+1,y)
                self.uncover(x+1,y+1)
    def set_flag(self, x, y):
        self.tiles[x][y].flag()

new_board = Board()
new_board.modify_size(11)
new_board.update_coords()
new_board.set_mines()
new_board.update_neighbours()
new_board.uncover(1,2)
new_board.uncover(4,5)
new_board.set_flag(5,7)
new_board.print_board()
