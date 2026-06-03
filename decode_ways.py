class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Time Complexity: O(N)
        - We iterate through the string `s` exactly once, taking O(1) operations per character.
        
        Space Complexity: O(1)
        - We only use two integer variables (`prev1`, `prev2`) to keep track of the previous states 
          instead of an entire DP array of size N.
        """
        if not s or s[0] == '0':
            return 0
            
        prev2 = 1 # Repreesents dp[i-2]
        prev1 = 1 # Represents dp[i-1]
        
        for i in range(1, len(s)):
            curr = 0
            
            # Single digit decoding (must be 1-9)
            if s[i] != '0':
                curr += prev1
                
            # Double digit decoding (must be 10-26)
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                curr += prev2
                
            # Move forward
            prev2 = prev1
            prev1 = curr
            
        return prev1
