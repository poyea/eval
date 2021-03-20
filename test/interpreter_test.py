import unittest
from eval.interpreter import Interpreter
from eval.parse import *
from eval.values import Number


class Tests_Interpreter(unittest.TestCase):
    def test_number(self):
        value = Interpreter().traverse(Number(107.11))
        self.assertEqual(value, Number(107.11))

    def test_addition(self):
        result = Interpreter().traverse(Add(Number(100), Number(1)))
        self.assertEqual(result.val, 101)

    def test_subtraction(self):
        result = Interpreter().traverse(Minus(Number(100), Number(1)))
        self.assertEqual(result.val, 99)
        result = Interpreter().traverse(Minus(Number(1), Number(100)))
        self.assertEqual(result.val, -99)

    def test_multiplication(self):
        result = Interpreter().traverse(Times(Number(3), Number(10)))
        self.assertEqual(result.val, 30)
        result = Interpreter().traverse(Times(Number(30), Number(8)))
        self.assertEqual(result.val, 240)

    def test_division(self):
        result = Interpreter().traverse(Divide(Number(50), Number(5)))
        self.assertEqual(result.val, 10)
        result = Interpreter().traverse(Divide(Number(22), Number(7)))
        self.assertAlmostEqual(result.val, 3.1428571429, 10)

    def test_integral_division(self):
        result = Interpreter().traverse(IntegralDivide(Number(50), Number(2)))
        self.assertEqual(result.val, 25)
        result = Interpreter().traverse(IntegralDivide(Number(31), Number(2)))
        self.assertAlmostEqual(result.val, 15)
        result = Interpreter().traverse(IntegralDivide(Number(127), Number(6)))
        self.assertAlmostEqual(result.val, 21)

    def test_exponential(self):
        result = Interpreter().traverse(Exponential(Number(10), Number(5)))
        self.assertEqual(result.val, 100000)
        result = Interpreter().traverse(Exponential(Number(2), Number(10.39)))
        self.assertAlmostEqual(result.val, 1341.8428456, 7)

        with self.assertRaises(Exception):
            Interpreter().traverse(Divide(Number(1), Number(0)))
