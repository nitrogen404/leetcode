class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        step1, step2 = 1, 1
        for i in range(2, n + 1):
            currentStep = step1 + step2
            step2, step1 = step1, currentStep
        return step1
