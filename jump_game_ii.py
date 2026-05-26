# ============================================================
# 45. Jump Game II
# ============================================================
# You are given a 0-indexed array of integers nums of length n. You are initially
# positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#   0 <= j <= nums[i] and
#   i + j < n
#
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].
#
# Example 1:
#   Input: nums = [2,3,1,1,4]
#   Output: 2
#   Explanation: The minimum number of jumps to reach the last index is 2.
#   Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
#   Input: nums = [2,3,0,1,4]
#   Output: 2
#
# Constraints:
#   1 <= nums.length <= 10^4
#   0 <= nums[i] <= 1000
#   It's guaranteed that you can reach the last index.
# ============================================================


# ---- Solution: Greedy (BFS-like interval updates) ----
def jump(nums: list[int]) -> int:
    """Return the minimum number of jumps to reach the last index of nums."""
    jumps = 0
    jump_level = 0
    max_level = 0

    # We iterate up to len(nums) - 1 because once we reach or pass the last index,
    # we don't need to jump any further.
    for i in range(len(nums) - 1):
        # Update the furthest index we can reach from all visited indices so far
        max_level = max(max_level, nums[i] + i)

        # Once we reach the end of the current jump's reach, we must take another jump
        # and update our boundary to the maximum reachable index.
        if i == jump_level:
            jumps += 1
            jump_level = max_level

    return jumps


# ============================================================
# Notes
# ============================================================
# Approach: Greedy (Implicit BFS / Interval Jump)
#   - We can think of this problem as maintaining an interval of indexes 
#     reachable with a certain number of jumps.
#   - `jump_level` represents the furthest index reachable with the current number of `jumps`.
#   - `max_level` represents the furthest index reachable overall from the current interval.
#   - We iterate through `nums` and continuously update `max_level`.
#   - When our pointer `i` reaches `jump_level` (the limit of our current jump range), 
#     we increment our jump count and extend our reach to `max_level`.
#
# Complexity Analysis:
#   - Time Complexity: O(n)
#     We traverse the `nums` array exactly once. For each element, we do constant time O(1) operations.
#   - Space Complexity: O(1)
#     We only use a few integer variables (`jumps`, `jump_level`, `max_level`) to track our progress,
#     requiring no extra storage.
# ============================================================


# ---- Tests ----
if __name__ == "__main__":
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([2, 3, 0, 1, 4]) == 2
    assert jump([0]) == 0
    assert jump([1, 2]) == 1
    assert jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]) == 2
    print("All tests passed!")
