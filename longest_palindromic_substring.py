# ============================================================
# 5. Longest Palindromic Substring
# ============================================================
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
#   Input: s = "babad"
#   Output: "bab"
#   Explanation: "aba" is also a valid answer.
#
# Example 2:
#   Input: s = "cbbd"
#   Output: "bb"
#
# Constraints:
#   1 <= s.length <= 1000
#   s consists of only digits and English letters.
# ============================================================


# ---- Solution: Expand Around Center ----
def longestPalindrome(s: str) -> str:
    """Return the longest palindromic substring in the input string s."""
    if not s:
        return ""

    start, end = 0, 0

    def expandAroundCenter(left: int, right: int) -> int:
        # Expand outward as long as characters match and indices are in bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Length of the palindrome found
        return right - left - 1

    for i in range(len(s)):
        # Case 1: Odd length palindromes centered at i (e.g. "aba")
        len1 = expandAroundCenter(i, i)
        # Case 2: Even length palindromes centered between i and i + 1 (e.g. "abba")
        len2 = expandAroundCenter(i, i + 1)
        
        max_len = max(len1, len2)

        # Update the boundaries of the longest palindrome found so far
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start : end + 1]


# ============================================================
# Notes
# ============================================================
# Approach: Expand Around Center
#   - A palindrome mirrors around its center. Therefore, a palindrome of length N 
#     has 2N - 1 possible centers (either at a character, or between two characters).
#   - We iterate through the string and consider each position as a potential center:
#     1. Center at `i` (representing odd length palindromes).
#     2. Center between `i` and `i + 1` (representing even length palindromes).
#   - For each center, we expand outward using helper `expandAroundCenter` and keep 
#     track of the maximum length seen.
#
# Why this beats Dynamic Programming:
#   - Standard DP takes O(N^2) Time and O(N^2) Space.
#   - Expand Around Center takes O(N^2) Time but only O(1) Auxiliary Space, making 
#     it much more memory-efficient.
#
# Complexity Analysis:
#   - Time Complexity: O(N^2)
#     We iterate N times over the string. For each index, expanding around the center 
#     takes O(N) time in the worst case.
#   - Space Complexity: O(1)
#     Only constant space is used to keep track of the start and end indices of the 
#     longest palindrome.
# ============================================================


# ---- Tests ----
if __name__ == "__main__":
    assert longestPalindrome("babad") in ["bab", "aba"]
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") == "a" or longestPalindrome("ac") == "c"
    assert longestPalindrome("racecar") == "racecar"
    print("All tests passed!")
