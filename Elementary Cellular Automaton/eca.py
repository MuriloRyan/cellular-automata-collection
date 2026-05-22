from bitarray import bitarray
from rules import RULES

class ElementaryCA:
    def __init__(
        self,
        rule: str,
        size: int = 256,
        seed: str = '1'
    ):
        if rule not in RULES:
            raise ValueError(
                f"Rule '{rule}' is not defined. "
                f"Available rules: {list(RULES.keys())}"
            )

        if len(seed) > size:
            raise ValueError(
                "Seed size cannot be larger than universe size."
            )

        self.rules = RULES[rule]
        self.size = size

        initial_state = bitarray('0' * size)

        start = (size - len(seed)) // 2

        for i, bit in enumerate(seed):
            initial_state[start + i] = int(bit)

        self.states = [initial_state]

    def generate(self):
        current_state = self.states[-1]
        next_state = bitarray()

        for index in range(self.size):
            L = current_state[index - 1] if index > 0 else 0
            C = current_state[index]
            R = current_state[index + 1] if (index + 1) < self.size else 0

            bits_to_check = (L << 2) | (C << 1) | R

            next_state.append(self.rules[bits_to_check])
        
        self.states.append(next_state)

