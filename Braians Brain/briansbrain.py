import random

class BrainsBrain:
    def __init__(self, width: int = 512, height: int = 512):
        self.width, self.height = width, height
        
        self.grid = [[0 for _ in range(self.height)] for _ in range(self.width)]
        self.next_grid = [[0 for _ in range(self.height)] for _ in range(self.width)]

        self.randomize()

    def randomize(self):
        self.grid = [
            [random.choices([0, 1, 2], weights=[90, 8, 2])[0]
            for _ in range(self.height)]
            for _ in range(self.width)
        ]

        self.next_grid = [column.copy() for column in self.grid]

    def step(self, x, y):
        
        cell = self.grid[x][y]

        match cell:
            case 0:
                neighbors = [
                    self.grid[x - 1][y - 1] if x > 0 and y > 0 else 0,
                    self.grid[x][y - 1] if y > 0 else 0,
                    self.grid[x + 1][y - 1] if x < self.width - 1 and y > 0 else 0,
                    self.grid[x - 1][y] if x > 0 else 0,
                    self.grid[x + 1][y] if x < self.width - 1 else 0,
                    self.grid[x - 1][y + 1] if x > 0 and y < self.height - 1 else 0,
                    self.grid[x][y + 1] if y < self.height - 1 else 0,
                    self.grid[x + 1][y + 1] if x < self.width - 1 and y < self.height - 1 else 0,
                ]
                actives = 0

                for n in neighbors:
                    if n == 1:
                        actives += 1

                if actives == 2:
                    self.next_grid[x][y] = 1
                else:
                    self.next_grid[x][y] = 0

            case 1:
                self.next_grid[x][y] = 2
                return
            
            case 2:
                self.next_grid[x][y] = 0
                return

    def update_grid(self):
        for x in range(self.width):
            for y in range(self.height):
                self.step(x, y)

        self.grid, self.next_grid = self.next_grid, self.grid