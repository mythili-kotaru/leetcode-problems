# ============================================================
# Longest Substring Without Repeating Characters
# ============================================================
# Given a string s, find the length of the longest substring
# without duplicate characters.
#
# Example 1: s = "abcabcbb" → 3  ("abc")
# Example 2: s = "bbbbb"   → 1  ("b")
# Example 3: s = "pwwkew"  → 3  ("wke")
#
# Constraints:
#   0 <= s.length <= 5 * 10^4
#   s consists of English letters, digits, symbols and spaces.
# ============================================================


# ---- Solution: Sliding Window ----
def longestSubStringWithoutRepeatingCharacters(s: str) -> int:
    seen = set()
    left = 0
    maxLen = 0  # initialize before the loop; handles empty string edge case

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        maxLen = max(maxLen, right - left + 1)

    return maxLen


# ============================================================
# Notes
# ============================================================
# Approach: Sliding Window
#   - Maintain a window [left, right] with no duplicate characters.
#   - Expand right each iteration; if s[right] is already in the
#     window, shrink from the left until the duplicate is removed.
#   - Track the maximum window size seen.
#
# Key insight: left only ever moves right, so both pointers
# traverse the string at most once → linear time.
#
# Time Complexity:  O(n)  — each character is added/removed at most once
# Space Complexity: O(min(n, α))  — set holds ≤ alphabet size α chars
# ============================================================


# ---- Tests ----
assert longestSubStringWithoutRepeatingCharacters("abcabcbb") == 3
assert longestSubStringWithoutRepeatingCharacters("bbbbb") == 1
assert longestSubStringWithoutRepeatingCharacters("pwwkew") == 3
assert longestSubStringWithoutRepeatingCharacters("") == 0        # edge: empty string
assert longestSubStringWithoutRepeatingCharacters("abcdef") == 6  # edge: no repeats
assert longestSubStringWithoutRepeatingCharacters("a") == 1       # edge: single char
print("All tests passed!")
