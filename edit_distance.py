class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Time Complexity: O(M * N) where M and N are lengths of word1 and word2.
        - We fill an (M+1) x (N+1) DP table.
        
        Space Complexity: O(M * N)
        - For the DP table. (Can be optimized to O(min(M, N)) using 1D array).
        """
        m = len(word1)
        n = len(word2)

        # Initialize DP table with 0s
        dp = [[0] * (n + 1) for i in range(m + 1)]
        
        # Base cases: if one string is empty, we must insert/delete all remaining characters
        for i in range(m + 1):
            dp[i][n] = m - i
        for j in range(n + 1):
            dp[m][j] = n - j

        # Fill DP table bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    # Characters match, no operation needed
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    # Characters don't match, take the minimum of 3 operations
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],    # Delete a character from word1
                        dp[i][j + 1],    # Insert a character into word1
                        dp[i + 1][j + 1] # Replace a character
                    )
                    
        return dp[0][0]
