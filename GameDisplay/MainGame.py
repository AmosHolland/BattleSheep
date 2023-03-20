import pygame
import math
import sys 

sys.path.append("..")

from GameSystem import GameBoard, GameHex, SheepStack


class BattleSheepGame:

    def __init__(self, players, screen):
        self.HEX_SIZE = 20
        self.GRASS_COLOUR = (0, 154, 23)


        self.screen = screen
        self.players = players 
        self.board = GameBoard.GameBoard()
    
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

    def make_dummy_board(self, grid):
        self.board.hex_board = grid
        

# Define the background colour
# using RGB color coding.
background_colour = (255, 255, 255)
  
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((1280, 720))

# Set the caption of the screen
pygame.display.set_caption('Battle Sheep')
  
# Fill the background colour to the screen
screen.fill(background_colour)

    

# Update the display using flip

  
# Variable to keep our game loop running
running = True
grid = [[0, 0, 0, 0, 0], [0, None, 0], [0, 0, 0]]

game = BattleSheepGame(2, screen)
game.make_dummy_board(grid)
game.draw_board()

pygame.display.flip()
# game loop
while running:
    
# for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False