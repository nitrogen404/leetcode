class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(start, array):
            if len(array) == k:
                result.append(array[:])
                return 
            for i in range(start, n + 1):
                array.append(i)
                backtrack(i + 1, array)
                array.pop()
        backtrack(1, [])
        return result