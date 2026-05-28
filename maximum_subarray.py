# ============================================================
# 53. Maximum Subarray
# ============================================================
# Given an integer array nums, find the subarray with the largest sum,
# and return its sum.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
# Example 1:
#   Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#   Output: 6
#   Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
# Example 2:
#   Input: nums = [1]
#   Output: 1
#
# Example 3:
#   Input: nums = [5,4,-1,7,8]
#   Output: 23
#
# Constraints:
#   1 <= nums.length <= 10^5
#   -10^4 <= nums[i] <= 10^4
# ============================================================


# ---- Solution: Kadane's Algorithm (Dynamic Programming) ----
def maxSubArray(nums: list[int]) -> int:
    """Return the maximum sum of a contiguous non-empty subarray."""
    if not nums:
        return 0

    max_sum = nums[0]
    current_sum = nums[0]

    for n in nums[1:]:
        # Decide whether to add the current number to the existing subarray
        # or start a new subarray beginning at the current number.
        current_sum = max(n, current_sum + n)
        # Record the maximum sum observed so far
        max_sum = max(max_sum, current_sum)

    return max_sum


# ============================================================
# Notes
# ============================================================
# Approach: Kadane's Algorithm
#   - At each step, we determine whether to continue the current subarray 
#     (`current_sum + n`) or start a new one at the current element (`n`).
#   - This is expressed as the dynamic programming relation:
#       current_sum[i] = max(nums[i], current_sum[i-1] + nums[i])
#
# Bug Fixes vs. Your Original Attempt:
#   1. Incorrect Handling of Negative-Only Arrays:
#      Your original code initialized `maxTotal = 0` and reset `total = 0` 
#      whenever `total < 0`. This works fine if there's at least one positive 
#      number in `nums`. However, if the array contains only negative numbers 
#      (e.g., `nums = [-1]`), your function would return `0` instead of `-1` 
#      (because the maximum single-element subarray `[-1]` has sum `-1`).
#      We corrected this by:
#        - Initializing `max_sum` and `current_sum` to `nums[0]`.
#        - Processing elements from index 1 onward and updating state dynamically.
#
# Complexity Analysis:
#   - Time Complexity: O(N)
#     We iterate through the list of length N exactly once, performing 
#     constant-time O(1) operations at each index.
#   - Space Complexity: O(1)
#     Only two scalar variables (`max_sum` and `current_sum`) are used, 
#     requiring constant auxiliary memory.
# ============================================================


# ---- Tests ----
if __name__ == "__main__":
    assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert maxSubArray([1]) == 1
    assert maxSubArray([5, 4, -1, 7, 8]) == 23
    # Edge case: All negative integers
    assert maxSubArray([-5, -4, -3, -2, -1]) == -1
    assert maxSubArray([-1, -2, -3]) == -1
    print("All tests passed!")
