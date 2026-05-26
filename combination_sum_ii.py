# ============================================================
# 40. Combination Sum II
# ============================================================
# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
#
# Example 1:
#   Input: candidates = [10,1,2,7,6,1,5], target = 8
#   Output:
#   [
#     [1,1,6],
#     [1,2,5],
#     [1,7],
#     [2,6]
#   ]
#
# Example 2:
#   Input: candidates = [2,5,2,1,2], target = 5
#   Output:
#   [
#     [1,2,2],
#     [5]
#   ]
#
# Constraints:
#   1 <= candidates.length <= 100
#   1 <= candidates[i] <= 50
#   1 <= target <= 30
# ============================================================


# ---- Solution: Backtracking with Duplicate Pruning ----
def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    # Sort the candidates to easily skip duplicate values and prune search paths
    candidates.sort()
    res = []

    def dfs(i: int, comb: list[int], total: int) -> None:
        if total == target:
            res.append(comb[:])  # Found a valid combination, append copy
            return
        
        if total > target or i >= len(candidates):
            return

        # Decision 1: Include candidates[i]
        comb.append(candidates[i])
        dfs(i + 1, comb, total + candidates[i])
        comb.pop()  # Backtrack

        # Decision 2: Exclude candidates[i]. To avoid duplicate combinations,
        # we must skip all subsequent elements that have the same value.
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(i + 1, comb, total)

    dfs(0, [], 0)
    return res


# ============================================================
# Notes
# ============================================================
# Approach: Backtracking (DFS) with Sorting & Duplicate Skip
#   - First, sort `candidates`. Sorting is crucial because:
#     1. It groups identical elements together, allowing easy duplicate skipping.
#     2. It allows early pruning (if `total + candidates[i] > target`, we can stop since all subsequent elements are larger).
#   - We use a recursive depth-first search (`dfs`) to construct combinations:
#     - Decision 1 (Include): Add the current candidate to `comb`, step to the next index `i + 1`.
#     - Decision 2 (Exclude): Pop the current candidate from `comb`, skip all duplicate elements (using a while loop), and then call `dfs` on the next unique element index.
#
# Complexity Analysis:
#   - Time Complexity: O(2^N)
#     In the worst case, each element can either be included or excluded in the combination.
#     This yields a recursion tree with a maximum of 2^N states. 
#     For each valid combination, copying it takes O(N) time.
#     Thus, the upper bound is O(N * 2^N).
#     (In practice, the search space is heavily pruned because total sum exceeds target quickly).
#
#   - Auxiliary Space: O(N)
#     The recursion stack goes at most N levels deep (where N is the number of candidates).
#     The `comb` array takes at most O(N) space.
#     Excluding the output list `res`, the auxiliary space complexity is O(N).
# ============================================================


# ---- Tests ----
if __name__ == "__main__":
    test1 = combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    expected1 = [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ]
    assert sorted(test1) == sorted(expected1), f"Expected {expected1}, but got {test1}"

    test2 = combinationSum2([2, 5, 2, 1, 2], 5)
    expected2 = [
        [1, 2, 2],
        [5]
    ]
    assert sorted(test2) == sorted(expected2), f"Expected {expected2}, but got {test2}"

    print("All tests passed!")
