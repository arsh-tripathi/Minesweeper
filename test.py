from minesweeper_oop import Tile, Board

def test_tile_creation():
    tile = Tile()
    assert not tile.is_bomb
    assert tile.face_value == "#"
    assert tile.display_value == 0

def test_set_bomb():
    tile = Tile()
    tile.set_bomb()
    assert tile.is_bomb
    assert tile.face_value == "#"
    assert tile.display_value == "B"

def test_set_coordinates():
    tile = Tile()
    tile.set_coordinates(2, 3)
    assert tile.x == 2
    assert tile.y == 3

def test_board_setup_board():
    board = Board()
    board.setup_board(5, 3)
    assert board.size == 5
    assert board.difficulty == 3
    assert len(board.tiles) == 5
    assert len(board.tiles[0]) == 5
    assert len(board.mine_locations) == 3

def test_board_uncover():
    board = Board()
    board.setup_board(5, 3)
    board.tiles[2][2].set_bomb()  # Set a bomb at (2, 2)
    board.uncover(2, 2)  # Uncover the tile
    assert board.tiles[2][2].display_value == "B"
    assert board.win_check() is False

def test_board_win_check():
    board = Board()
    board.setup_board(9,0)
    assert board.win_check() is False
    # Uncover all non-bomb tiles
    for i in range(board.size):
        for j in range(board.size):
            if (i, j) not in board.mine_locations:
                board.uncover(i, j)
    assert board.win_check() is True

# Run the test functions
test_tile_creation()
test_set_bomb()
test_set_coordinates()
test_board_setup_board()
test_board_uncover()
test_board_win_check()
