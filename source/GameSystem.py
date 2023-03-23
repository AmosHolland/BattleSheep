import GameBoard
import BoardMaker

class GameSystem:

    def __init__(self):

        self.board = GameBoard.GameBoard()
        self.players = 2
        self.board_maker = BoardMaker.BoardMaker(self.players, self.board) 

        self.player_colours = [(255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0)]
        self.player_points = [0, 0, 0, 0]
        self.player_can_play = [True, True, True, True]
        
        self.game_over = False
        self.is_building = False
    
    def get_board(self):
        return_board = self.board.hex_board

        if self.is_building:
            available_coords = self.get_available_coords()
            for x, y in available_coords:
                return_board[x][y] = "available"
        
        return return_board
    
    def start_building(self):
        self.board_maker = BoardMaker.BoardMaker(self.players, self.board)
        self.is_building = True
    
    def get_available_coords(self):
        return self.board_maker.get_available_spaces().keys()
    




    
        

