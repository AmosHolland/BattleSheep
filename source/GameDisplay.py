import pygame
import pygame_menu
import math

import GameBoard, GameHex, SheepStack


class GameDisplay:

    def __init__(self):
        self.HEX_SIZE = 20
        self.GRASS_COLOUR = (13, 55, 13)
        self.BACKGROUND_COLOUR = (255, 255, 255)


        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Battle Sheep') 

        self.board = GameBoard.GameBoard()
        self.players = 2

        self.home_screen()
    
    def set_players(self, players):
        print(players)
        self.players = int(players[0])
        print(self.players)

    def draw_hex(self, centre_x, centre_y):
        vertices = []
        for i in range(6):
            angle = (math.pi / 180) * (60 * i)
            vertices.append((centre_x + self.HEX_SIZE * math.cos(angle), centre_y + self.HEX_SIZE * math.sin(angle)))

        pygame.draw.polygon(self.screen, self.GRASS_COLOUR, vertices)

        prev = vertices[0]
        for i in range(1, 6):
            pygame.draw.line(self.screen, (0,0,0), prev, vertices[i])
            prev = vertices[i]
        
        pygame.draw.line(self.screen, (0,0,0), vertices[0], vertices[5])
    
    def draw_board(self):
        self.screen.fill(self.BACKGROUND_COLOUR)

        centre_x = self.HEX_SIZE
        hex_board = self.board.hex_board
        print(hex_board)
        for x in range(len(hex_board)):
            if x % 2 == 0:
                centre_y = self.HEX_SIZE
            else:
                centre_y = 0.5 * math.sqrt(3) * self.HEX_SIZE + self.HEX_SIZE
            for y in range(len(hex_board[x])):
                if hex_board[x][y] != None:
                    self.draw_hex(centre_x, centre_y)
                centre_y += math.sqrt(3) * self.HEX_SIZE
            centre_x += 1.5 * self.HEX_SIZE
        
        pygame.display.flip()

        
    def make_dummy_board(self, grid):
        self.board.hex_board = grid
    
    def home_screen(self):

        self.screen.fill(self.BACKGROUND_COLOUR)
        pygame.display.flip()

        self.make_dummy_board([[0,0,0,0,0],[0,None,0,0,0],[0,0,0,None,0]])
        main_menu = pygame_menu.Menu("Battle Sheep", 500, 500)
        main_menu.add.selector("Players: ", ["2", "3", "4"], onchange=self.set_players)
        main_menu.add.button("Play", self.draw_board)
        main_menu.add.button("Quit", pygame_menu.events.EXIT)
        main_menu.mainloop(self.screen)
    

pygame.init()
display = GameDisplay()