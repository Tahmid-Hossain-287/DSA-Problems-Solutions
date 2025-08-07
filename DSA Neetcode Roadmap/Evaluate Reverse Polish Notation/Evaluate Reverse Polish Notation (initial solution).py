import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : operator.floordiv,
        }

        answer = None
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in operators:
                # you have numbers on your stack. use the operator on them.
                operation = operators[tokens[i]]
                if len(stack) == 2:
                    answer = operation(stack[0], stack[1])
                    stack.clear()
                else:
                    answer = operation(answer, stack[0])
                    stack.clear()
            else:
                stack.append(int(tokens[i]))
        return answer