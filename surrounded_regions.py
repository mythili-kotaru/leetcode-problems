from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
            
        m, n = len(board), len(board[0])
        
        def dfs(i, j):
            # If out of bounds or the cell is not an 'O', stop.
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            
            # Mark the cell as 'U' (Unsurrounded) so we know it shouldn't be flipped
            board[i][j] = 'U'
            
            # Explore all 4 adjacent directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        # Step 1: Run DFS on all boundary 'O's and mark them as 'U'
        for i in range(m):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][n - 1] == 'O': dfs(i, n - 1)
            
        for j in range(n):
            if board[0][j] == 'O': dfs(0, j)
            if board[m - 1][j] == 'O': dfs(m - 1, j)
            
        # Step 2 & 3: Re-evaluate the entire board
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    # If it's still 'O', it means it was not connected to a boundary, so it's surrounded.
                    board[i][j] = 'X'
                elif board[i][j] == 'U':
                    # If it's 'U', it was connected to a boundary, so we revert it back to 'O'.
                    board[i][j] = 'O'

'''
Time Complexity: O(M * N)
- Where M is the number of rows and N is the number of columns.
- The DFS is only called on 'O' cells and immediately changes them to 'U'. Each cell is visited at most a constant number of times. The subsequent loops iterate through all cells exactly once.

Space Complexity: O(M * N)
- This is the maximum space required for the call stack during the depth-first search in the worst-case scenario (e.g., if the entire board is filled with 'O's).
'''
