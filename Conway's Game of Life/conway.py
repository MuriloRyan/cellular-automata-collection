import random
import numpy

class Cell:
    def __init__(self, initial_state: int):
        self.state: int = initial_state #1 means life, 0 means death

class Grid:
    def __init__(self):
        self.grid = []

    def generate_grid(self, horizontal: int, vertical: int):
        self.grid = [[Cell(random.choice([0, 1])) for _ in range(horizontal)] for _ in range(vertical)]
        self.horizontal = horizontal
        self.vertical = vertical

        return self

    def update_grid(self):
        # Create a new grid to store the next state
        next_grid = [[Cell(cell.state) for cell in row] for row in self.grid]

        for x in range(self.horizontal -1):
            for y in range(self.vertical -1):
                nb1, nb2, nb3 = self.grid[x-1][y+1], self.grid[x][y+1], self.grid[x +1][y+1]
                nb4, main, nb5 = self.grid[x-1][y], self.grid[x][y], self.grid[x +1][y]
                nb6, nb7, nb8 = self.grid[x-1][y-1], self.grid[x][y-1], self.grid[x +1][y-1]

                to_check = [nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8]
                live_neighbors = 0
                for i in to_check:
                    if isinstance(i, Cell):
                        if i.state == 1:
                            live_neighbors += 1

                if main.state == 1:
                    if live_neighbors < 2:
                        next_grid[x][y].state = 0
                    elif live_neighbors == 2 or live_neighbors == 3:
                        next_grid[x][y].state = 1
                    elif live_neighbors > 3:
                        next_grid[x][y].state = 0
                elif main.state == 0:
                    if live_neighbors == 3:
                        next_grid[x][y].state = 1 
                    else:
                        next_grid[x][y].state = 0

        self.grid = next_grid
        return self
    