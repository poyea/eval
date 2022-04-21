from eval.interpreter import Interpreter
from eval.lexer import Lexer
from eval.parse import Parser


def evaluate(expression):
    try:
        user_input = expression
        lexer = Lexer(user_input)
        parser = Parser(lexer.generate_tokens())
        tree = parser.parse()
        if not tree:
            raise Exception("Unable to parse")
        interpreter = Interpreter()
        value = interpreter.traverse(tree)
        return value
    except Exception as e:
        return e
