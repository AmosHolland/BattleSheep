class SheepStack:

    def __init__(self, size, team):
        self.size = size
        self.team = team
    
    def split(self, new_size):
        if new_size >= self.size:
            print("Error!")

        else:
            new_stack = SheepStack(new_size)
            self.size -= new_size
            return new_stack
