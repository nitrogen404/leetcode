class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = deque()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        # Top and bottom rows
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                q.append((0, i))
                board[0][i] = 'S'

            if board[len(board) - 1][i] == 'O':
                q.append((len(board) - 1, i))
                board[len(board) - 1][i] = 'S'


        # Left and right columns
        for i in range(len(board)):
            if board[i][0] == 'O':
                q.append((i, 0))
                board[i][0] = 'S'

            if board[i][len(board[0]) - 1] == 'O':
                q.append((i, len(board[0]) - 1))
                board[i][len(board[0]) - 1] = 'S'
            
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 'O':
                    board[nr][nc] = 'S'
                    q.append((nr, nc))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'