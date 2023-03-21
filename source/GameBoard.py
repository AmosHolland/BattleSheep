import GameHex

class GameBoard:

    def __init__(self):

        self.hex_board = [[None for i in range(75)] for j in range(75)]
    
    def add_hex(self, x, y):
        neighbours = [self.hex_board[x][y + 1], self.hex_board[x + 1][y], self.hex_board[x + 1][y - 1], self.hex_board[x][ y - 1], self.hex_board[x - 1][y - 1], self.hex_board[x - 1][y]]
        new_hex = GameHex.GameHex(neighbours)
    
