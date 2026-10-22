class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        rows = len(board)
        cols = len(board[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            
            if board[r][c] == ".":
                return 

            board[r][c] = "."
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)
        
        ships = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    ships += 1
                    dfs(r, c)
        return ships