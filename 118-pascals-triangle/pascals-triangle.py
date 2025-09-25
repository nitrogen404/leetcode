class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row in range(numRows):
            r = [1] * (row + 1)
            for j in range(1, row):
                r[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
            triangle.append(r)
        return triangle