from eval.tokens import Token, TokenEnum

SKIP = " \r\t\n"
DIGITS = "1234567890"


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in SKIP:
                self.advance()
            elif self.current_char == "." or self.current_char in DIGITS:
                yield self.generate_numbers()
            elif self.current_char == "+":
                self.advance()
                yield Token(TokenEnum.PLUS)
            elif self.current_char == "-":
                self.advance()
                yield Token(TokenEnum.MINUS)
            elif self.current_char == "*":
                self.advance()
                if self.current_char == "*":
                    self.advance()
                    yield Token(TokenEnum.EXPONENTIAL)
                else:
                    yield Token(TokenEnum.MULTIPLY)
            elif self.current_char == "/":
                self.advance()
                if self.current_char == "/":
                    self.advance()
                    yield Token(TokenEnum.INTEGRAL_DIVIDE)
                else:
                    yield Token(TokenEnum.DIVIDE)
            elif self.current_char == "(":
                self.advance()
                yield Token(TokenEnum.LPAREN)
            elif self.current_char == ")":
                self.advance()
                yield Token(TokenEnum.RPAREN)
            else:
                raise Exception(f"Invalid character {self.current_char}")

    def generate_numbers(self):
        decimal_count = 0
        num_str = self.current_char
        self.advance()

        while self.current_char != None and (
            self.current_char == "." or self.current_char in DIGITS
        ):
            if self.current_char == ".":
                decimal_count += 1
                if decimal_count > 1:
                    raise "ea"

            num_str += self.current_char
            self.advance()

        if num_str.startswith("."):
            num_str = "0" + num_str
        if num_str.endswith("."):
            num_str += "0"

        return Token(TokenEnum.NUMBER, float(num_str))
