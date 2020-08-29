from lib.lexer import Lexer
from lib.parse import Parser
from lib.interpreter import Interpreter


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
