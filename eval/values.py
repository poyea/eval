from dataclasses import dataclass


@dataclass
class Number:
    val: float

    def __repr__(self):
        return f"{self.val}"
