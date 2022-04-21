from dataclasses import dataclass

from eval.tokens import TokenEnum


@dataclass
class Number:
    val: float

    def __repr__(self):
        return f"{self.val}"


@dataclass
class Add:
    num_a: any
    num_b: any

    def __repr__(self):
        return f"({self.num_a}+{self.num_b})"


@dataclass
class Minus:
    num_a: any
    num_b: any

    def __repr__(self):
        return f"({self.num_a}-{self.num_b})"


@dataclass
class Times:
    num_a: any
    num_b: any

    def __repr__(self):
        return f"({self.num_a}*{self.num_b})"


@dataclass
class Divide:
    num_a: any
    num_b: any

    def __repr__(self):
        return f"({self.num_a}/{self.num_b})"


@dataclass
class IntegralDivide:
    num_a: any
    num_b: any

    def __repr__(self):
        return f"({self.num_a}//{self.num_b})"


@dataclass
class Exponential:
    num_a: any
    num_b: any

    def __repr__(self):
        return f"({self.num_a}**{self.num_b})"


@dataclass
class Positive:
    val: any

    def __repr__(self):
        return f"(+{self.val})"


@dataclass
class Negative:
    val: any

    def __repr__(self):
        return f"(-{self.val})"


class Parser:
    def __init__(self, tokens):
        self.tockens = iter(tokens)
        self.advance()

    def advance(self):
        try:
            self.current_token = next(self.tockens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token == None:
            return None
        result = self.expr()

        if self.current_token != None:
            raise Exception("Invalid syntax")

        return result

    def expr(self):
        result = self.terms()

        while self.current_token != None and self.current_token.type in (
            TokenEnum.PLUS,
            TokenEnum.MINUS,
        ):
            if self.current_token.type == TokenEnum.PLUS:
                self.advance()
                result = Add(result, self.terms())
            elif self.current_token.type == TokenEnum.MINUS:
                self.advance()
                result = Minus(result, self.terms())

        return result

    def terms(self):
        result = self.factor()

        while self.current_token != None and self.current_token.type in (
            TokenEnum.MULTIPLY,
            TokenEnum.DIVIDE,
            TokenEnum.INTEGRAL_DIVIDE,
            TokenEnum.EXPONENTIAL,
        ):
            if self.current_token.type == TokenEnum.MULTIPLY:
                self.advance()
                result = Times(result, self.factor())
            elif self.current_token.type == TokenEnum.DIVIDE:
                self.advance()
                result = Divide(result, self.factor())
            elif self.current_token.type == TokenEnum.INTEGRAL_DIVIDE:
                self.advance()
                result = IntegralDivide(result, self.factor())
            elif self.current_token.type == TokenEnum.EXPONENTIAL:
                self.advance()
                result = Exponential(result, self.factor())

        return result

    def factor(self):
        token = self.current_token
        if token.type == TokenEnum.LPAREN:
            self.advance()
            result = self.expr()
            if self.current_token.type != TokenEnum.RPAREN:
                raise Exception()
            self.advance()
            return result
        if token.type == TokenEnum.NUMBER:
            self.advance()
            return Number(token.val)
        elif token.type == TokenEnum.PLUS:
            self.advance()
            return Positive(self.factor())
        elif token.type == TokenEnum.MINUS:
            self.advance()
            return Negative(self.factor())
        raise Exception()
