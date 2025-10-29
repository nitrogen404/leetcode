class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        currentRow = 0
        direction = -1
        for c in s:
            rows[currentRow] += c
            if currentRow == 0 or currentRow == numRows - 1:
                direction *= -1
            currentRow += direction 
        return ''.join(rows)