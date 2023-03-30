import pygame
import pygame_menu
import math

import GameBoard, GameHex, SheepStack, GameSystem


class GameDisplay:

    def __init__(self):
        self.HEX_SIZE = 20
        self.GRASS_COLOUR = (13, 55, 13)
        self.BACKGROUND_COLOUR = (255, 255, 255)


        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Battle Sheep') 

        self.game_system = GameSystem.GameSystem()
        self.players = 2

        self.coord_map = {}

        self.home_screen()
    
    def set_players(self, players):
        self.players = int(players[0])

    def draw_hex(self, centre_x, centre_y, colour):
        vertices = []
        for i in range(6):
            angle = (math.pi / 180) * (60 * i)
            vertices.append((centre_x + self.HEX_SIZE * math.cos(angle), centre_y + self.HEX_SIZE * math.sin(angle)))

        pygame.draw.polygon(self.screen, colour, vertices)

        prev = vertices[0]
        for i in range(1, 6):
            pygame.draw.line(self.screen, (0,0,0), prev, vertices[i])
            prev = vertices[i]
        
        pygame.draw.line(self.screen, (0,0,0), vertices[0], vertices[5])
    
    def draw_board(self):
        self.screen.fill(self.BACKGROUND_COLOUR)

        centre_x = 3 * self.HEX_SIZE
        hex_board = self.game_system.get_board()
        started_drawing = False

        for x in range(len(hex_board)):
            if x % 2 == 0:
                centre_y = 3 * self.HEX_SIZE
            else:
                centre_y = 0.5 * math.sqrt(3) * self.HEX_SIZE + self.HEX_SIZE
            for y in range(len(hex_board[x])):
                if hex_board[x][y] != None:
                    started_drawing = True
                    self.coord_map[(x, y)] = (centre_x, centre_y)
                    if hex_board[x][y] == "available":
                        self.draw_hex(centre_x, centre_y, (255, 255, 67)) 
                    else:
                        self.draw_hex(centre_x, centre_y, self.GRASS_COLOUR)
                if started_drawing:
                    centre_y += math.sqrt(3) * self.HEX_SIZE
            if started_drawing:
                centre_x += 1.5 * self.HEX_SIZE
        
        pygame.display.flip()

    def check_new_hex_collisions(self, x, y):
        inner_radius = self.HEX_SIZE * (math.sqrt(3) / 2)
        available_hex_centres = self.game_system.get_available_coords()

        for centre_x, centre_y in available_hex_centres:
            real_x, real_y = self.coord_map[(centre_x, centre_y)]

            if ((x - real_x) ** 2) + ((y - real_y) ** 2) < inner_radius ** 2:
                return (centre_x, centre_y)
        
        return None
    
    def make_dummy_board(self, grid):
        self.game_system.board.hex_board = grid
    
    def home_screen(self):

        self.screen.fill(self.BACKGROUND_COLOUR)
        pygame.display.flip()

        main_menu = pygame_menu.Menu("Battle Sheep", 500, 500)
        main_menu.add.selector("Players: ", ["2", "3", "4"], onchange=self.set_players)
        main_menu.add.button("Play", self.make_board)
        main_menu.add.button("Quit", pygame_menu.events.EXIT)
        main_menu.mainloop(self.screen)
    
    def make_board(self):
        
        self.game_system.start_building()
        
        running = True
        while self.game_system.is_building and running:

            self.draw_board()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    clicked_hex_coords =  self.check_new_hex_collisions(x, y)
                    if clicked_hex_coords != None:
                        self.pick_placement_centre(clicked_hex_coords)
                if event.type == pygame.QUIT:
                    running = False

    def pick_placement_centre(self, coords):
        configurations = self.game_system.get_coord_configs(coords)
        
        

pygame.init()
display = GameDisplay()