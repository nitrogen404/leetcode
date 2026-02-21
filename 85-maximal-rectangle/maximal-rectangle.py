class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        extended = heights + [0]
        
        for i in range(len(extended)):
            while stack and extended[stack[-1]] >= extended[i]:
                h = extended[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)
        
        return max_area