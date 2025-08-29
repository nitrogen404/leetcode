class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        for row in matrix:
            if row[0] <= target <= row[-1]:
                return self.search(row, target)
        return False

    def search(self, row, target):
        low, high = 0, len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
            