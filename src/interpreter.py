from lib.parse import *
from lib.values import Number


class Interpreter:
    def traverse(self, node):
        method_name = f"traverse_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def traverse_Number(self, node):
        return Number(node.val)

    def traverse_Add(self, node):
        return Number(self.traverse(node.num_a).val + self.traverse(node.num_b).val)

    def traverse_Minus(self, node):
        return Number(self.traverse(node.num_a).val - self.traverse(node.num_b).val)

    def traverse_Times(self, node):
        return Number(self.traverse(node.num_a).val * self.traverse(node.num_b).val)

    def traverse_Divide(self, node):
        try:
            return Number(self.traverse(node.num_a).val / self.traverse(node.num_b).val)
        except:
            raise Exception("Divide by 0 exception")

    def traverse_Exponential(self, node):
        result, base, power = (
            1,
            self.traverse(node.num_a).val,
            int(self.traverse(node.num_b).val),
        )
        while power > 0:
            if power & 1:
                result *= base
            power >>= 1
            base *= base
        return Number(result)

    def traverse_Positive(self, node):
        return self.traverse(node.val)

    def traverse_Negative(self, node):
        return Number(-self.traverse(node.val).val)
