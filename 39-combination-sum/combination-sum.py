class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index, target, array):
            if target == 0:
                result.append(array[:])
                return 
            for i in range(index, len(candidates)):
                if candidates[i] <= target:
                    array.append(candidates[i])
                    backtrack(i, target - candidates[i], array)
                    array.pop()
        backtrack(0, target, [])
        return result