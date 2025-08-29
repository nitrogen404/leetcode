class Solution:
    def isHappy(self, n: int) -> bool:
        memory = set()
        current = str(n)
        while current not in memory:
            memory.add(current)
            sum_ = 0
            for digit in current:
                sum_ += int(digit) ** 2
            if sum_ == 1:
                return True
            current = str(sum_)
        return False