import unittest
from lib.lexer import Lexer
from lib.tokens import Token, TokenEnum


class Tests_Lexer(unittest.TestCase):
    def test_empty(self):
        tokens = list(Lexer("").generate_tokens())
        self.assertEqual(tokens, [])

    def test_skip(self):
        tokens = list(Lexer("\r").generate_tokens())
        self.assertEqual(tokens, [])
        tokens = list(Lexer("\r\n").generate_tokens())
        self.assertEqual(tokens, [])
        tokens = list(Lexer("\n").generate_tokens())
        self.assertEqual(tokens, [])
        tokens = list(Lexer("\t").generate_tokens())
        self.assertEqual(tokens, [])
        tokens = list(Lexer("  ").generate_tokens())
        self.assertEqual(tokens, [])

    def test_numbers(self):
        tokens = list(Lexer(". 1 2.3 4.56 7. .8").generate_tokens())
        self.assertEqual(
            tokens,
            [
                Token(TokenEnum.NUMBER, 0),
                Token(TokenEnum.NUMBER, 1),
                Token(TokenEnum.NUMBER, 2.3),
                Token(TokenEnum.NUMBER, 4.56),
                Token(TokenEnum.NUMBER, 7),
                Token(TokenEnum.NUMBER, 0.8),
            ],
        )

    def test_symbols(self):
        tokens = list(Lexer("+-*/()**").generate_tokens())
        self.assertEqual(
            tokens,
            [
                Token(TokenEnum.PLUS),
                Token(TokenEnum.MINUS),
                Token(TokenEnum.MULTIPLY),
                Token(TokenEnum.DIVIDE),
                Token(TokenEnum.LPAREN),
                Token(TokenEnum.RPAREN),
                Token(TokenEnum.EXPONENTIAL),
            ],
        )
