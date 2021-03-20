from dataclasses import dataclass
from enum import Enum


class TokenEnum(Enum):
    LPAREN = 0
    RPAREN = 1
    NUMBER = 2
    PLUS = 3
    MINUS = 4
    MULTIPLY = 5
    DIVIDE = 6
    INTEGRAL_DIVIDE = 7
    EXPONENTIAL = 8


@dataclass
class Token:
    type: TokenEnum
    val: any = None

    def __repr__(self):
        if self.val != None:
            return self.type.name + f":{self.val}"
        else:
            return ""
