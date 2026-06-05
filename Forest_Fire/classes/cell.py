class Cell:
    def __init__(self, state: int = 0, age: int = 0, has_food: bool = False) -> None:
        self.state = state
        self.age = age
        self.has_food = has_food

    def copy(self):
        return Cell(self.state, self.age, self.has_food)

    def __repr__(self) -> str:
        return f"Cell(state={self.state}, age={self.age}, has_food={self.has_food})"
