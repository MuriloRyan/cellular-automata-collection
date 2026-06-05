import random
import copy

class Cell:
    def __init__(self, state: int = 0, age: int = 0, has_food: bool = False) -> None:
        self.state = state
        self.age = age
        self.has_food = has_food

class ForestFire:
    def __init__(self, horizontal_size: int = 64, vertical_size: int = 64, seed: int | None = None) -> None:
        if seed is not None:
            random.seed(seed)

        self.grid = [[Cell() for _ in range(vertical_size)] for _ in range(horizontal_size)]
        self.next_grid = [[Cell() for _ in range(vertical_size)] for _ in range(horizontal_size)]

        self.horizontal_size = horizontal_size
        self.vertical_size = vertical_size

        self.f = 0.00005 # probability of lightning strike
        self.p = 0.01 # probability of a tree growing
    
    def generate_forest(self, density: float = 0.5):
        for x in range(self.horizontal_size):
            for y in range(self.vertical_size):
                if random.random() < density:
                    self.grid[x][y] = Cell(1)

        return self.grid

    def get_cell(self, x: int, y: int):
        if x < 0 or y < 0: return Cell(0)
        
        try:
            return self.grid[x][y]
        except IndexError:
            return Cell(0)

    def growing(self, x: int, y: int):
        if random.random() < self.p:
            self.next_grid[x][y] = Cell(1)

        return self.next_grid[x][y]
    
    def lightning(self, x: int, y: int):
        if random.random() < self.f:
            self.next_grid[x][y] = Cell(2)

        return self.next_grid[x][y]

    def spread_fire(self, x: int, y: int):
        """ _______________
            | NE | N | NO |
            | L | ? | O |
            | LE | S | SO |
            _______________ """

        nb1, nb2, nb3 = self.get_cell(x-1, y+1), self.get_cell(x, y+1), self.get_cell(x +1, y+1)
        nb4, _, nb5 = self.get_cell(x-1, y), self.get_cell(x, y), self.get_cell(x +1, y)
        nb6, nb7, nb8 = self.get_cell(x-1, y-1), self.get_cell(x, y-1), self.get_cell(x +1, y-1)

        to_check = [nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8]
        for cell in to_check:
            if isinstance(cell, Cell):
                # if one of the surrounding cells is on fire, the current cell will catch fire
                if cell.state == 2:
                    self.next_grid[x][y] = Cell(2)
                    break

        return self.next_grid[x][y]

    def stop_fire(self, x: int, y: int):
        self.next_grid[x][y] = Cell(0)

        return self.next_grid[x][y]
    
    def grow_food(self, x: int, y: int):
        if random.random() < self.p:
            self.next_grid[x][y].has_food = True

        return self.next_grid[x][y]
    
    def cycle(self):
        next_state = copy.deepcopy(self.grid)

        for x in range(self.horizontal_size):
            for y in range(self.vertical_size):

                if self.grid[x][y].state == 1:
                    self.grid[x][y].age += 1

                    if self.lightning(x, y).state == 2:
                        next_state[x][y] = Cell(2)
                
                    else:
                        next_state[x][y] = self.spread_fire(x, y)
                
                elif self.grid[x][y].state == 2:
                    next_state[x][y] = self.stop_fire(x, y)
                
                elif self.grid[x][y].state == 0:
                    next_state[x][y] = self.growing(x, y)
            

        self.grid = next_state
        return next_state

