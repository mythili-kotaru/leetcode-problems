# ============================================================
# Longest Palindromic Substring
# ============================================================
# Given a string s, return the longest palindromic substring in s.
#
# Example 1: s = "babad" → "bab"  (or "aba")
# Example 2: s = "cbbd"  → "bb"
#
# Constraints:
#   1 <= s.length <= 1000
#   s consist of only digits and English letters.
# ============================================================


# ---- Solution: Expand Around Center ----
def longestPalindromicSubstring(s: str) -> str:
    result = ""

    for i in range(len(s)):

        # Odd-length palindromes (single center character)
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > len(result):
                result = s[left:right + 1]
            left -= 1   # expand outward EVERY iteration, not just when we update max
            right += 1

        # Even-length palindromes (two adjacent center characters)
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > len(result):
                result = s[left:right + 1]
            left -= 1
            right += 1

    return result  # return is OUTSIDE the for loop


# ============================================================
# Notes
# ============================================================
# Approach: Expand Around Center
#   - Every palindrome has a center (single char or pair of chars).
#   - For each index i, try expanding outward from both center types.
#   - Keep track of the longest valid palindrome found.
#
# Bug fixes vs. original attempt:
#   1. `return` moved outside the for loop (was returning after i=0 only)
#   2. `right < len(s)` instead of `right <= len(s)` (prevented IndexError)
#   3. `left -= 1` / `right += 1` moved outside the `if` block
#      (inside the if caused an infinite loop when window ≤ current max)
#   4. Odd/even labels corrected (i,i = odd center; i,i+1 = even center)
#   5. Return the actual substring, not just its length
#
# Time Complexity:  O(n²) — n centers × O(n) expansion each
# Space Complexity: O(1)  — no extra data structures (result slice is output)
# ============================================================


# ---- Tests ----
assert longestPalindromicSubstring("babad") in ("bab", "aba")
assert longestPalindromicSubstring("cbbd") == "bb"
assert longestPalindromicSubstring("a") == "a"          # edge: single char
assert longestPalindromicSubstring("ac") in ("a", "c")  # edge: no palindrome > 1
assert longestPalindromicSubstring("racecar") == "racecar"  # whole string
assert longestPalindromicSubstring("abacaba") == "abacaba"  # whole string
print("All tests passed!")
