# ============================================================
# 49. Group Anagrams
# ============================================================
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
#
# Example 1:
#   Input: strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
#   Input: strs = [""]
#   Output: [[""]]
#
# Example 3:
#   Input: strs = ["a"]
#   Output: [["a"]]
#
# Constraints:
#   1 <= strs.length <= 10^4
#   0 <= strs[i].length <= 100
#   strs[i] consists of lowercase English letters.
# ============================================================

from collections import defaultdict


# ---- Solution: Sorting Keys with Hash Map ----
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """Group all anagrams in strs together and return them as a list of lists."""
    hm = defaultdict(list)

    for st in strs:
        # Sort characters to form a unique key for anagrams
        key = tuple(sorted(st))
        hm[key].append(st)

    # Return all grouped lists
    return list(hm.values())


# ============================================================
# Notes
# ============================================================
# Approach: Categorization by Sorted Characters
#   - Two words are anagrams if and only if their sorted character sequences are identical.
#   - We can sort each string to generate a canonical "key" (stored as a hashable tuple).
#   - A hash map (`defaultdict(list)`) maps each sorted key to the list of original strings.
#
# Bug Fixes vs. Your Original Attempt:
#   1. Missing Return Statement:
#      Your original code built the `hm` dictionary successfully but did not return anything.
#      We added `return list(hm.values())` to retrieve the grouped lists of anagrams.
#   2. Syntax / Indentation Error:
#      There was a leading space in your import line (` from collections ...`) which throws 
#      an `IndentationError` in Python. We corrected this indentation.
#
# Optimization Idea (Character Counting):
#   - Instead of sorting the string of length L (which takes O(L log L) time), we can 
#     build a letter frequency list of size 26 (e.g. `[0]*26`) to represent the string key.
#     This reduces the key generation step to O(L) time, yielding O(N * L) total time complexity.
#
# Complexity Analysis:
#   - Time Complexity: O(N * L log L)
#     Where N is the number of strings and L is the maximum length of a string in `strs`.
#     We iterate through N strings, and sorting each takes O(L log L) time.
#
#   - Space Complexity: O(N * L)
#     We store every string in our hash map `hm`, consuming space proportional to the 
#     total length of all characters across all strings.
# ============================================================


# ---- Tests ----
if __name__ == "__main__":
    # Helper to sort groups and items inside groups for comparison
    def canonical_repr(groups: list[list[str]]) -> list[list[str]]:
        return sorted([sorted(g) for g in groups])

    test1 = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert canonical_repr(test1) == canonical_repr(expected1)

    test2 = groupAnagrams([""])
    expected2 = [[""]]
    assert canonical_repr(test2) == canonical_repr(expected2)

    test3 = groupAnagrams(["a"])
    expected3 = [["a"]]
    assert canonical_repr(test3) == canonical_repr(expected3)

    print("All tests passed!")
