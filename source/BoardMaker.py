import GameBoard

class BoardMaker:

    def __init__(self, players, board):
        self.tiles = players * 4
        self.board = board
        self.available_spaces = {(38, 38) : [True, False, False, False]}
    
    def add_tile(self, place_index):
        if self.tiles == 0:
            print ("Board finished.")
            return self.board

        x, y = self.available_spaces[place_index][1]
        tile_piece = self.available_spaces[place_index][0]

        self.board.add_hex(x, y)

        if tile_piece == 0:
            self.board.add_hex(x + 1, y - 1)
            self.board.add_hex(x, y - 1)
            self.board.add_hex(x - 1, y)

        if tile_piece == 1:
            self.board.add_hex(x + 1, y)
            self.board.add_hex(x + 2, y - 1)
            self.board.add_hex(x + 1, y - 1)

        if tile_piece == 2:
            self.board.add_hex(x - 1, y + 1)
            self.board.add_hex(x, y + 1)
            self.board.add_hex(x + 1, y)
        
        if tile_piece == 3:
            self.board.add_hex(x - 1, y)
            self.board.add_hex(x - 2, y + 1)
            self.board.add_hex(x - 1, y + 1)

        self.tiles -= 1
        self.make_available_spaces()

        return self.board

    def make_available_spaces(self):
        self.available_spaces = {}

        # increments and extra_hexes for certain positions and directions in hex grid
        increments = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]
        extra_hexes = [[(1, -1), (0, -1), (-1, 0)], [(1, 0),(2, -1),(1, -1)], [(-1, 1), (0, 1), (1, 0)], [(-1, 0), (-2, 1), (-1, 1)]]

        # for all spaces in our hex board
        for x in range(75):
            for y in range(75):

                # if there is currently a hex in the space
                if self.board.hex_board[x][y] != None:

                    current_hex = self.board.hex_board[x][y]

                    # for all spaces adjacent to the hex
                    for i in range(6):

                        # if the space is empty
                        if current_hex.neighbours[i] == None:
                            new_x = x + increments[i][0]
                            new_y = y + increments[i][1]

                            # for all different ways you could add a tile to this place
                            for j in range(4):
                                valid_tile = True 

                                # check that the spaces that the new tile will be placed in are empty
                                for k in extra_hexes[j]:
                                    check_x = new_x + k[0]
                                    check_y = new_y + k[1]
                                    valid_tile = valid_tile and self.board.hex_board[check_x][check_y] == None

                                # if this configuration is valid, add it as an available space
                                if valid_tile:
                                    if (new_x, new_y) not in self.available_spaces:
                                        self.available_spaces[(new_x, new_y), [False, False, False, False]]
                                    self.available_spaces[(new_x, new_y)][j] = True 

        return self.available_spaces

    def get_board(self):
        return self.board

    def get_available_spaces(self):
        return self.available_spaces




