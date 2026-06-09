class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Determines if s3 is formed by an interleaving of s1 and s2.
        
        Solution Explanation (Dynamic Programming - Bottom Up):
        - `dp[i][j]` represents whether the suffix of s3 starting at `i + j` can be 
          formed by interleaving the suffix of s1 starting at `i` and s2 starting at `j`.
        - We iterate backwards from the ends of the strings down to index 0.
        - For each state (i, j), we check if taking a character from s1 or s2 
          matches the target string s3, and if the remaining substrings can be interleaved.
        
        Time Complexity: O(m * n)
        Where m is len(s1) and n is len(s2). We fill an (m+1) x (n+1) grid, 
        with each state taking O(1) time to compute.
        
        Space Complexity: O(m * n)
        Used by the 2D DP array. (Note: this can be optimized to O(n) space 
        by only storing the current and next row).
        """
        m = len(s1)
        n = len(s2)
        k = len(s3)
        
        if m + n != k:
            return False

        dp = [[False]* (n+1) for i in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n:
                    continue
                    
                if i < m and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < n and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
                    
        return dp[0][0]
