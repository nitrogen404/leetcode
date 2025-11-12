class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memory = {}
        def dfs(index, currentSum):
            key = (index, currentSum)
            if key in memory:
                return memory[key]

            if index == len(nums):
                return 1 if currentSum == target else 0

            plus = dfs(index + 1, nums[index] + currentSum)
            minus = dfs(index + 1, currentSum - nums[index])
            memory[key] = plus + minus
            return memory[key]
        return dfs(0, 0)

        
