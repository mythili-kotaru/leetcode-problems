# # scratchpadiven an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true


def wordboard(board,word):
    res = []
    visited = set()
    m = len(board)
    n = len(board[0])

    def dfs(i,j,pos):
        if pos == len(word) - 1:
            return True 

        if i < 0 or j < 0 or i >= m or j >= n or (i,j) in visited or board[i][j] != word[pos]:
            return 
        
        visited.add(i,j)

        dfs(i + 1, j, pos + 1)
        dfs(i - 1, j, pos + 1)
        dfs(i, j - 1, pos + 1)
        dfs(i, j + 1, pos + 1)

    dfs(0,0,0)
    return False 
