class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalTank = 0
        currentTankState = 0
        start = 0
        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            currentTankState += gain
            totalTank += gain
            if currentTankState < 0:
                start = i + 1
                currentTankState = 0
        return start if totalTank >= 0 else -1
