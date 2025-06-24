class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closing_opening = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in closing_opening.keys() and stack:
                if stack[-1] == closing_opening[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False