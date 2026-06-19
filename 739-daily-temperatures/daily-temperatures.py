class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                previous_temp = stack.pop()
                answer[previous_temp] = i - previous_temp
            stack.append(i)
        return answer
