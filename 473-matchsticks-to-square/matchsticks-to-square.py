class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0 or len(matchsticks) < 4:
            return False
        side = total // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4
        
        def backtrack(index):
            if index == len(matchsticks):
                for i in range(4):
                    if sides[i] != side:
                        return False
                return True

            current = matchsticks[index]
            for i in range(4):
                if sides[i] + current <= side:
                    sides[i] += current
                    if backtrack(index + 1):
                        return True
                    sides[i] -= current
                if sides[i] == 0:
                    break
            return False
        return backtrack(0)