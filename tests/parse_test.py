import unittest

from eval.parse import *
from eval.tokens import Token, TokenEnum


class Tests_Parser(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Parser([]).parse(), None)

    def test_parser(self):
        self.assertEqual(Parser([Token(TokenEnum.NUMBER, 0)]).parse(), Number(0))
        self.assertEqual(Parser([Token(TokenEnum.NUMBER, 1.2)]).parse(), Number(1.2))
        self.assertEqual(Parser([Token(TokenEnum.NUMBER, -0.3)]).parse(), Number(-0.3))

    def test_operations(self):
        self.assertEqual(
            Parser(
                [
                    Token(TokenEnum.NUMBER, -0.3),
                    Token(TokenEnum.PLUS),
                    Token(TokenEnum.NUMBER, 0.3),
                ]
            ).parse(),
            Add(Number(-0.3), Number(0.3)),
        )
        self.assertEqual(
            Parser(
                [
                    Token(TokenEnum.NUMBER, 3),
                    Token(TokenEnum.MINUS),
                    Token(TokenEnum.NUMBER, 3),
                ]
            ).parse(),
            Minus(Number(3), Number(3)),
        )
        self.assertEqual(
            Parser(
                [
                    Token(TokenEnum.NUMBER, 5),
                    Token(TokenEnum.MULTIPLY),
                    Token(TokenEnum.NUMBER, 6),
                ]
            ).parse(),
            Times(Number(5), Number(6)),
        )
        self.assertEqual(
            Parser(
                [
                    Token(TokenEnum.NUMBER, 50),
                    Token(TokenEnum.DIVIDE),
                    Token(TokenEnum.NUMBER, 10),
                ]
            ).parse(),
            Divide(Number(50), Number(10)),
        )
        self.assertEqual(
            Parser(
                [
                    Token(TokenEnum.NUMBER, 50),
                    Token(TokenEnum.DIVIDE),
                    Token(TokenEnum.NUMBER, 10),
                    Token(TokenEnum.PLUS),
                    Token(TokenEnum.NUMBER, 0.3),
                ]
            ).parse(),
            Add(Divide(Number(50), Number(10)), Number(0.3)),
        )
        self.assertEqual(
            Parser(
                [
                    Token(TokenEnum.NUMBER, 2),
                    Token(TokenEnum.EXPONENTIAL),
                    Token(TokenEnum.NUMBER, 10),
                    Token(TokenEnum.PLUS),
                    Token(TokenEnum.NUMBER, 0.3),
                ]
            ).parse(),
            Add(Exponential(Number(2), Number(10)), Number(0.3)),
        )
        self.assertEqual(
            Parser(
                [
                    Token(TokenEnum.LPAREN),
                    Token(TokenEnum.NUMBER, 127),
                    Token(TokenEnum.INTEGRAL_DIVIDE),
                    Token(TokenEnum.NUMBER, 6),
                    Token(TokenEnum.MINUS),
                    Token(TokenEnum.NUMBER, 11),
                    Token(TokenEnum.PLUS),
                    Token(TokenEnum.NUMBER, 7),
                    Token(TokenEnum.RPAREN),
                    Token(TokenEnum.EXPONENTIAL),
                    Token(TokenEnum.NUMBER, 10),
                    Token(TokenEnum.INTEGRAL_DIVIDE),
                    Token(TokenEnum.NUMBER, 3),
                ]
            ).parse(),
            IntegralDivide(
                Exponential(
                    Add(
                        Minus(IntegralDivide(Number(127), Number(6)), Number(11)),
                        Number(7),
                    ),
                    Number(10),
                ),
                Number(3),
            ),
        )
