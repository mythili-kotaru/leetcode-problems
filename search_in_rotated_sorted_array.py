# ============================================================
# 33. Search in Rotated Sorted Array
# ============================================================
# Given an integer array nums sorted in ascending order (with distinct
# values) that has been possibly rotated at an unknown pivot, and an
# integer target, return the index of target or -1 if not found.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1: nums = [4,5,6,0,1,2], target = 0  → 3
# Example 2: nums = [4,5,6,7,0,1,2], target = 3 → -1
# Example 3: nums = [1], target = 0              → -1
# ============================================================


# ---- Solution: Modified Binary Search ----
def sortedArraySearch(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:  # Bug fix: must be <= to check the last remaining element
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half [left..mid] is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half [mid..right] is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# ============================================================
# Notes
# ============================================================
# Approach: Modified Binary Search
#   - A rotated sorted array has one key property: at least one
#     half (left or right of mid) is ALWAYS sorted.
#   - We figure out which half is sorted, then check if target
#     falls within that sorted range.
#   - If yes → search that half.  If no → search the other half.
#
# Why <= on left/right but < on mid in the range checks:
#   - nums[left] <= target  → target could BE nums[left]
#   - target < nums[mid]    → we already checked nums[mid] == target
#     above and it wasn't, so we exclude mid with strict <
#   - Same logic for the right half: nums[mid] < target <= nums[right]
#
# Bug fix from original:
#   - while left < right → while left <= right
#     With strict <, when left == right we skip checking the last
#     remaining element and wrongly return -1.
#
# Complexity:
#   - Time:  O(log N) — binary search, halving the search space each step
#   - Space: O(1) — only a few integer variables
# ============================================================


# ---- Tests ----
assert sortedArraySearch([4, 5, 6, 0, 1, 2], 0) == 3
assert sortedArraySearch([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert sortedArraySearch([1], 0) == -1
assert sortedArraySearch([1], 1) == 0
assert sortedArraySearch([3, 1], 1) == 1
assert sortedArraySearch([5, 1, 3], 5) == 0
print("All tests passed!")
