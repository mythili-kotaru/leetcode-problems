# ============================================================
# 46. Permutations
# ============================================================
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
#
# Example 1:
#   Input: nums = [1,2,3]
#   Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Example 2:
#   Input: nums = [0,1]
#   Output: [[0,1],[1,0]]
#
# Example 3:
#   Input: nums = [1]
#   Output: [[1]]
#
# Constraints:
#   1 <= nums.length <= 6
#   -10 <= nums[i] <= 10
#   All the integers of nums are unique.
# ============================================================


# ---- Solution: Backtracking (DFS with Boolean Tracking) ----
def permutations(nums: list[int]) -> list[list[int]]:
    """Return all possible permutations of the input list of distinct integers."""
    res = []
    # Track which elements are already in the current combination (O(1) lookups)
    used = [False] * len(nums)

    def dfs(comb: list[int]) -> None:
        # Base Case: Current combination is complete
        if len(comb) == len(nums):
            res.append(comb[:])  # Append a copy of the combination list
            return

        for i, num in enumerate(nums):
            if used[i]:
                continue

            # Choose the element
            used[i] = True
            comb.append(num)
            
            # Recurse
            dfs(comb)
            
            # Backtrack (Undo the choice)
            comb.pop()
            used[i] = False

    dfs([])
    return res


# ============================================================
# Notes
# ============================================================
# Approach: Backtracking (DFS)
#   - We build permutations incrementally. For each position, we iterate through 
#     all numbers and pick one that hasn't been used yet.
#   - We recurse to build the rest of the permutation, and backtrack by 
#     deselecting the element once the recursion returns.
#
# Bug Fixes vs. Your Original Attempt:
#   1. Undefined variable `i` & Type Error: 
#      Your original code used `res.append("".join(nums[i]))`. Since `nums` contains 
#      integers, calling `"".join()` would throw a `TypeError`. Additionally, the 
#      variable `i` was undefined. This is fixed by appending a copy of the current 
#      list: `res.append(comb[:])`.
#   2. Performance Optimization (O(1) vs O(N) Lookup):
#      Your code checked element presence using `if num in comb`, which performs 
#      a linear search of O(N) time at each step. By introducing a boolean array 
#      `used`, we achieve O(1) state lookup, which significantly speeds up execution.
#
# Complexity Analysis:
#   - Time Complexity: O(N * N!)
#     The number of leaves in the recursion tree is exactly N! (the number of permutations).
#     At each leaf, we copy the permutation of size N, taking O(N) time.
#     The total time is bounded by O(N * N!).
#
#   - Auxiliary Space: O(N)
#     The recursion stack goes at most N levels deep. The `used` array and the `comb` 
#     array both require O(N) memory.
# ============================================================


# ---- Tests ----
if __name__ == "__main__":
    assert sorted(permutations([1, 2, 3])) == sorted([
        [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
    ])
    assert sorted(permutations([0, 1])) == sorted([[0, 1], [1, 0]])
    assert permutations([1]) == [[1]]
    print("All tests passed!")
