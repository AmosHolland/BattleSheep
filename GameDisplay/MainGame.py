import pygame
import math

def draw_hex(centre_x, centre_y, size, surface):
    vertices = []
    for i in range(6):
        angle = (math.pi / 180) * (60 * i)
        vertices.append((centre_x + size * math.cos(angle), centre_y + size * math.sin(angle)))

    pygame.draw.polygon(surface, (0, 154, 23), vertices)

    prev = vertices[0]
    for i in range(1, 6):
        pygame.draw.line(surface, (0,0,0), prev, vertices[i])
        prev = vertices[i]

    pygame.draw.line(surface, (0,0,0), vertices[5], vertices[0])

def draw_hex_grid(width, height, size, surface):
    centre_x = size
    for x in range(width):
        if x % 2 == 0:
            centre_y = size 
        else:
            centre_y = 0.5 * math.sqrt(3) * size + size
        for y in range(height):
            draw_hex(centre_x, centre_y, size, surface)
            centre_y += math.sqrt(3) * size
        centre_x += 1.5 * size
        

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
grid = [[0, 0, 0, 0, 0], [0, 0, 0], [0, 0, 0]]
draw_hex_grid(20, 30, 15, screen)

pygame.display.flip()
# game loop
while running:
    
# for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False