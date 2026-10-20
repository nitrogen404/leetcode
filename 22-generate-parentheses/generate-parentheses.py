class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(s, openbrackets, closebrackets):
            if len(s) == 2 * n:
                result.append(s)
                return 
            if openbrackets < n:
                backtrack(s + '(', openbrackets + 1, closebrackets)
            if closebrackets < openbrackets:
                backtrack(s + ')', openbrackets, closebrackets + 1)
        backtrack("", 0, 0)
        return result