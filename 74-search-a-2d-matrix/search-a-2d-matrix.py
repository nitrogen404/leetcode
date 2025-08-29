class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        low, high = 0, len(matrix) * len(matrix[0]) - 1
        while low <= high:
            mid = (low + high) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            value = matrix[row][col]
            if value == target:
                return True
            if value < target:
                low = mid + 1
            else:
                high = mid - 1
        return False