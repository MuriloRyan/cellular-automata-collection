import random
from abc import ABC, abstractmethod
from typing import Any

class ForestBase(ABC):
    def __init__(self, horizontal_size: int = 64, vertical_size: int = 64, seed: int | None = None) -> None:
        if seed is not None:
            random.seed(seed)

        self.horizontal_size = horizontal_size
        self.vertical_size = vertical_size

        self.grid = [[self.cell_factory() for _ in range(vertical_size)] for _ in range(horizontal_size)]
        self.next_grid = [[self.cell_factory() for _ in range(vertical_size)] for _ in range(horizontal_size)]

    @abstractmethod
    def cell_factory(self) -> Any:
        raise NotImplementedError

    def get_cell(self, x: int, y: int):
        if x < 0 or y < 0:
            return self.cell_factory()

        try:
            return self.grid[x][y]
        except IndexError:
            return self.cell_factory()
