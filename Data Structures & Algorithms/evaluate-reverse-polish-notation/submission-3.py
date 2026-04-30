class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid_ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: math.trunc(x / y)
        }
        for token in tokens:
            if token in valid_ops:
                op1 = stack.pop()
                op2 = stack.pop()
                op = valid_ops[token]
                stack.append(op(op2, op1))

            else:
                stack.append(int(token))
            print(stack)
        return stack[0]