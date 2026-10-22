from collections import deque
class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        rows = len(board)
        cols = len(board[0]) 
        
        ships = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    if r > 0 and board[r - 1][c] == "X": # above
                        continue
                    if c > 0 and board[r][c - 1] == "X":
                        continue
                    ships += 1
        return ships
"""
[
["X","X",".","X"],
["X",".",".","X"],
[".",".",".","X"]
]

 def dfs(r, c):
            if board[r][c] == ".":
                return

            grid[r][c] = "."
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "X":
                    board[nr][nc] = "."
            
            return True


"""