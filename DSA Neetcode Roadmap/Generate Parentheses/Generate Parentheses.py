class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []
        
        def solution_function(openN, closeN):
            if openN > closeN:
                stack.append(")")
                solution_function(openN, closeN+1)
                stack.pop()
            if openN < n:
                stack.append("(")
                solution_function(openN+1,closeN)
                stack.pop()
            if openN == closeN == n:
                res.append("".join(stack))
                return

        solution_function(0, 0)
        return res
