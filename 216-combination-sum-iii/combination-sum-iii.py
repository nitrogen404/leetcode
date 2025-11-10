class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtrack(start, array, total):
            if len(array) == k:
                if total == n:
                    result.append(array[:])
                return 
            
            for i in range(start, 10):
                if total + i > n:
                    break
                array.append(i)
                backtrack(i + 1, array, total + i)
                array.pop()
        backtrack(1, [], 0)
        return result
                