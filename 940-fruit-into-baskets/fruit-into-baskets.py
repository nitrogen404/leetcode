class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        memory = {}
        l, maxLen = 0, 0
        for r in range(len(fruits)):
            if fruits[r] in memory:
                memory[fruits[r]] += 1
            else:
                memory[fruits[r]] = 1
            while len(memory) > 2:
                memory[fruits[l]] -= 1
                if memory[fruits[l]] == 0:
                    del memory[fruits[l]]
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen            