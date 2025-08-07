import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : operator.truediv,
        }

        answer = None
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in operators:
                # you have numbers on your stack. use the operator on them.
                operation = operators[tokens[i]]
                right_element = stack.pop()
                left_element = stack.pop()
                stack.append(int(operation(left_element, right_element)))
            else:
                stack.append(int(tokens[i]))
        return stack[0]
