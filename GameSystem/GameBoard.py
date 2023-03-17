import GameHex

class GameBoard:

    def __init__(self):

        self.hex_board = [[]]

        for x in range (75):
            for y in range(75):
                self.hex_board[x][y] = None
    
    def add_hex(self, x, y):
        neighbours = [self.hex_board[x][y + 1], self.hex_board[x + 1][y], self.hex_board[x + 1][y - 1], self.hex_board[x][ y - 1], self.hex_board[x - 1][y - 1], self.hex_board[x - 1][y]]
        new_hex = GameHex.GameHex(neighbours)
    

