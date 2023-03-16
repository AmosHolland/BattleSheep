class GameBoard:

    def __init__(self, root_tile):

        coords = root_tile.get_coords(0, 0)
        x_min = 0
        y_min = 0

        for i in coords:
            x = i[1]
            y = i[2]

            if x < x_min:
                x_min = x
            if y < y_min:
                y_min = y
        
        self.board = [[]]

        for i in coords:
            self.board[i[2] - y_min][i[1] - x_min] = i[0]
        
