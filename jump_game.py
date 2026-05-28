# ============================================================
# 55. Jump Game
# ============================================================
# You are given an integer array nums. You are initially positioned at the 
# array's first index, and each element in the array represents your 
# maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
# Example 1:
#   Input: nums = [2,3,1,1,4]
#   Output: true
#   Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
#   Input: nums = [3,2,1,0,4]
#   Output: false
#   Explanation: You will always arrive at index 3 no matter what. Its maximum 
#                jump length is 0, which makes it impossible to reach the last index.
#
# Constraints:
#   1 <= nums.length <= 10^4
#   0 <= nums[i] <= 10^5
# ============================================================


# ---- Solution: Greedy (Backward Goal Post Shifting) ----
def canJump(nums: list[int]) -> bool:
    """Return True if you can reach the last index, False otherwise."""
    n = len(nums)
    # The final index we want to reach is our initial goal
    goal = n - 1

    # Iterate backwards from the second-to-last index to the first index
    for i in range(n - 2, -1, -1):
        # If we can reach or exceed the current goal from index i,
        # index i becomes our new goal post.
        if i + nums[i] >= goal:
            goal = i

    # If the goal post shifted all the way to index 0, we can reach the end
    return goal == 0


# ============================================================
# Notes
# ============================================================
# Approach: Greedy Backward Search
#   - We work backward from the target index (`n - 1`).
#   - We maintain a `goal` index representing the closest index from which we 
#     know we can reach the end.
#   - For each index `i`, if `i + nums[i] >= goal`, it means we can reach our 
#     current goal from index `i`. Therefore, we update `goal = i`.
#   - At the end of the loop, if `goal == 0`, it means we can reach the final 
#     index starting from the first index.
#
# Bug Fixes vs. Your Original Attempt:
#   1. Incorrect Goal Assignment (`goal = i - 1`):
#      In your code, you set `goal = i - 1`. If we can reach the goal from `i`, 
#      then `i` itself becomes the new destination we must reach from earlier steps. 
#      Setting `goal = i - 1` skips index `i` entirely and incorrectly shifts the goalpost.
#      We corrected this to `goal = i`.
#   2. Incorrect Inequality Check (`>` instead of `>=`):
#      You checked if `i + nums[i] > goal`. However, landing exactly at the goal 
#      (`i + nums[i] == goal`) is sufficient to transition. We corrected this to `>=`.
#   3. Loop Range starting at `n - 1`:
#      You ran the loop starting at the final index `n - 1`. Since the goal is 
#      already `n - 1`, we can start checking from `n - 2`.
#
# Complexity Analysis:
#   - Time Complexity: O(N)
#     We perform a single backward pass of the array of length N, doing O(1) work per element.
#   - Space Complexity: O(1)
#     We only use a single integer variable (`goal`), requiring constant space.
# ============================================================


# ---- Tests ----
if __name__ == "__main__":
    assert canJump([2, 3, 1, 1, 4]) == True
    assert canJump([3, 2, 1, 0, 4]) == False
    assert canJump([0]) == True
    assert canJump([2, 0]) == True
    assert canJump([1, 0, 1, 0]) == False
    print("All tests passed!")
