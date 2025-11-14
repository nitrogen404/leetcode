class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag_1 = set()
        diag_2 = set()

        def backtrack(row):
            if row == n:
                snapshot = ["".join(r) for r in board]
                result.append(snapshot)
                return 
            for col in range(n):
                if col in cols or (row + col) in diag_1 or (row - col) in diag_2:
                    continue
                board[row][col] = "Q"
                cols.add(col)
                diag_1.add(row + col)
                diag_2.add(row - col)
                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diag_1.remove(row + col)
                diag_2.remove(row - col)
        backtrack(0)
        return result

