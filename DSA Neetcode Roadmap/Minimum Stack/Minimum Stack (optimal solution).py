class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []

    def push(self, val: int) -> None:
        if not(self.stack) and not(self.minimum_stack):
            self.minimum_stack.append(val)
            return self.stack.append(val)
        elif val < self.minimum_stack[-1]:
            self.minimum_stack.append(val)
            self.stack.append(val)
        else:
            self.minimum_stack.append(self.minimum_stack[-1])
            self.stack.append(val)
        return self.stack[-1]

    def pop(self) -> None:
        if self.minimum_stack:
            self.minimum_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not(self.minimum_stack):
            return self.stack[-1]
        return self.minimum_stack[-1]
