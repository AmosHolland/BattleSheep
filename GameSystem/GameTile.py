class GameTile:

    def __init__(self, neighbours):
        self.neighbours = neighbours
        self.can_move = []
        for i in range(6):
            self.can_move[i] = not self.neighbours[i] == None
            self.neighbours[i].add_neighbour(self, ((i + 3) % 6))
        
        self.stack = None
        self.has_stack = False 
        self.visited = False
    
    def add_neighbour(self, new_neighbour, direction):
        self.neighbours[direction] = new_neighbour

    def check_move(self, direction):
        if self.can_move(direction):
            return self.neighbours[direction].check_move(direction)
        else:
            return self
    
    def move_into(self, stack, direction):
        if self.stack != None:
            print("Error!")
        else:
            self.stack = stack 
            self.neighbours[((direction + 3) % 6)].block(direction)
    
    def block(self, direction):
        self.can_move[direction] = False
    
    def move_from(self, size, direction):
        new_stack = self.stack.split(size)
        new_cell = self.neighbours[direction].check_move(direction)
        new_cell.move_into(new_stack, direction)
    
    def get_coords(self, x, y):
        self.visited = True
        coord_list = []
        to_visit = []
        increments = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]

        for i in range(6):
            if self.neighbours[i] != None:
                if not self.neighbours[i].visited:
                    to_visit.append((i, self.neighbours[i]))
                    self.neighbours[i].visited = True
        
        for i in range(len(to_visit)):
            x_inc, y_inc = increments[to_visit[i][0]]
            new_coords = to_visit[i][1].get_coords(x + x_inc, y + y_inc)
            coord_list = coord_list + new_coords
        
        coord_list.append((self, x, y))

        return coord_list
    # For visualisation run a thing to get co-ords for all the tiles at the start of the game
    # (relative to eachother)
    # Using this info - either:
    #   - Put all the tiles into a 2D array relative to their co-ordinates
    #   - Store the co-ordinates of each tile in the tile
    # Then to visualise iterate through this - get info for each tile from the tile object
