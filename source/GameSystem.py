import GameBoard

class GameSystem:

    def __init__(self):

        self.board = GameBoard.GameBoard()

        self.players = 2
        self.player_colours = [(255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0)]
        self.player_points = [0, 0, 0, 0]
        self.player_can_play = [True, True, True, True]
        
        self.game_over = False 

    def take_turn(self):
        for i in range(self.players):
            if self.player_can_play[i]:
                # take turn
                pass
        
        # check if players can play
        game_not_over = True
        for i in self.player_can_play:
            game_not_over = game_not_over and i
        
        self.game_over = not game_not_over
        

