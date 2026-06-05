import random
import copy

try:
    from ..classes.forest_base import ForestBase
except ImportError:
    from classes.forest_base import ForestBase

class SimpleFire(ForestBase):
    def cell_factory(self):
        return 0

    def __init__(self, horizontal_size: int = 64, vertical_size: int = 64, seed: int | None = None) -> None:
        super().__init__(horizontal_size, vertical_size, seed)
        self.f = 0.0005  # probability of lightning strike
        self.p = 0.01  # probability of a tree growing

    def generate_forest(self, density: float = 0.5):
        for x in range(self.horizontal_size):
            for y in range(self.vertical_size):
                if random.random() < density:
                    self.grid[x][y] = 1

        return self.grid

    def growing(self, x: int, y: int):
        if random.random() < self.p:
            self.next_grid[x][y] = 1

        return self.next_grid[x][y]

    def lightning(self, x: int, y: int):
        if random.random() < self.f:
            self.next_grid[x][y] = 2

        return self.next_grid[x][y]

    def spread(self, x: int, y: int):
        nb1, nb2, nb3 = self.get_cell(x - 1, y + 1), self.get_cell(x, y + 1), self.get_cell(x + 1, y + 1)
        nb4, nb5 = self.get_cell(x - 1, y), self.get_cell(x + 1, y)
        nb6, nb7, nb8 = self.get_cell(x - 1, y - 1), self.get_cell(x, y - 1), self.get_cell(x + 1, y - 1)

        for cell in (nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8):
            if cell == 2:
                self.next_grid[x][y] = 2
                break

        return self.next_grid[x][y]

    def stop_fire(self, x: int, y: int):
        self.next_grid[x][y] = 0
        return self.next_grid[x][y]

    def cycle(self):
        next_state = copy.deepcopy(self.grid)

        for x in range(self.horizontal_size):
            for y in range(self.vertical_size):
                current = self.grid[x][y]

                if current == 1:
                    if self.lightning(x, y) == 2:
                        next_state[x][y] = 2
                    else:
                        next_state[x][y] = self.spread(x, y)
                elif current == 2:
                    next_state[x][y] = self.stop_fire(x, y)
                elif current == 0:
                    next_state[x][y] = self.growing(x, y)

        self.grid = next_state
        return next_state
