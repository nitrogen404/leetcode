class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        prevSmaller = self.pse(heights)
        nextSmaller = self.nse(heights)
        for i in range(len(heights)):
            area = (nextSmaller[i] - prevSmaller[i] - 1) * heights[i]
            maxArea = max(maxArea, area)
        return maxArea

    def pse(self, heights):
        stack = []
        result = [-1] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(i)
        return result
    
    def nse(self, heights):
        stack = []
        result = [len(heights)] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                index = stack.pop()
                result[index] = i
            stack.append(i)
        return result