class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        nse = self.nse(heights)
        pse = self.pse(heights)
        for i in range(len(heights)):
           
            area = (nse[i] - pse[i] - 1) * heights[i]
            maxArea = max(area, maxArea)
        return maxArea
    

    def nse(self, heights):
        nextSmaller = [len(heights)] * len(heights)
        stk = []
        for i in range(len(heights)):
            while stk and heights[stk[-1]] >= heights[i]:
                index = stk.pop()
                nextSmaller[index] = i
            stk.append(i)
        return nextSmaller
    
    def pse(self, heights):
        prevSmaller = [-1] * len(heights)
        stk = []
        for i in range(len(heights)):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk:
                prevSmaller[i] = stk[-1]
            stk.append(i)
        return prevSmaller

