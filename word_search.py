from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Time Complexity: O(M * N * 4^L)
        - M is the number of rows, N is the number of columns, L is the length of the word.
        - We iterate through M * N starting cells. From each, we can branch out in 4 directions, 
          up to L times.
        
        Space Complexity: O(L)
        - The recursion stack will go as deep as the length of the word L.
        - The `visited` set will store at most L elements at any given time.
        """
        m = len(board)
        n = len(board[0])
        visited = set()

        def dfs(i, j, pos):
            # If the current cell is out of bounds, already visited, or doesn't match the required character
            if (i < 0 or j < 0 or i >= m or j >= n or 
                (i, j) in visited or board[i][j] != word[pos]):
                return False
            
            # If we matched all characters up to the last one, we found the word
            if pos == len(word) - 1:
                return True
            
            # Mark as visited for the current path
            visited.add((i, j))

            # Explore all 4 adjacent directions
            res = (dfs(i + 1, j, pos + 1) or
                   dfs(i - 1, j, pos + 1) or
                   dfs(i, j - 1, pos + 1) or
                   dfs(i, j + 1, pos + 1))

            # Backtrack: unmark the cell so it can be visited in other paths
            visited.remove((i, j))

            return res

        # We must try starting the DFS from EVERY cell in the grid
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
                    
        return False