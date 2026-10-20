class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(s, opencount, closedcount):
            if len(s) == 2 * n:
                result.append(s)
                return 
            if opencount < n:
                backtrack(s + "(", opencount + 1, closedcount)
            if closedcount < opencount:
                backtrack(s + ")", opencount, closedcount + 1)
        backtrack("", 0, 0)
        return result