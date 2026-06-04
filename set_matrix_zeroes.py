from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        Time Complexity: O(M * N) where M and N are dimensions of the matrix.
        Space Complexity: O(M + N) for the `rows` and `cols` arrays. 
        (Note: It can be optimized to O(1) by using the first row and column of the matrix as flags).
        """
        m = len(matrix)
        n = len(matrix[0])

        rows = [False] * m
        cols = [False] * n

        # Pass 1: find all rows and columns that need to be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        # Pass 2: zero out the rows
        for i in range(m):
            if rows[i]:
                for j in range(n):
                    matrix[i][j] = 0
        
        # Pass 3: zero out the columns
        for j in range(n):
            if cols[j]:
                for i in range(m):
                    matrix[i][j] = 0
