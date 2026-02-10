class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = 0
        stack = []
        ple = [-1] * len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                ple[i] = stack[-1]
            stack.append(i)
        

        stack = []
        nse = [len(arr)] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        
        for i in range(len(arr)):
            leftCount = i - ple[i]
            rightCount =  nse[i] - i
            result = (result + arr[i] * leftCount * rightCount) % (10**9 + 7)
        return result