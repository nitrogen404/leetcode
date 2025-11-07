class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(index, target, array):
            if target == 0:
                result.append(array[:])
                return 
            for i in range(index, len(candidates)):
                if candidates[i] != candidates[i - 1] or index == i:
                    if candidates[i] <= target:
                        array.append(candidates[i])
                        backtrack(i + 1, target - candidates[i], array)
                        array.pop()
                    elif candidates[i] > target:
                        break
        backtrack(0, target, [])
        return result 