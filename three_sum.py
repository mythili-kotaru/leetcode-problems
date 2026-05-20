# ============================================================
# 3Sum
# ============================================================
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1: nums = [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]
# Example 2: nums = [0,1,1]          → []
# Example 3: nums = [0,0,0]          → [[0,0,0]]
# ============================================================


# ---- Solution: Sort and Two Pointers ----
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):
        # Skip duplicate values for the first element to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two pointers: left starts just after i, right at the end
        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                # Found a triplet summing to 0 (we store values, not indices)
                res.append([nums[i], nums[left], nums[right]])

                # Move pointers past duplicates for the second and third elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Crucial step: actually move the pointers to new elements
                left += 1
                right -= 1

    return res


# ============================================================
# Notes
# ============================================================
# Approach: Sort & Two Pointers
#   - First, sort the array. This allows us to use two pointers to find pairs.
#   - Fix the first element `nums[i]`. If `nums[i] > 0`, we can stop early 
#     because any subsequent positive numbers cannot sum to 0.
#   - Use a two-pointer approach (`left = i + 1`, `right = len-1`) to find two 
#     numbers that sum to `-nums[i]`.
#   - To prevent duplicate triplets:
#     1. Skip `i` if `nums[i] == nums[i-1]`.
#     2. When `total == 0`, skip duplicate `left` and `right` elements before 
#        moving them.
#
# Bug Fixes vs. Your Original Attempt:
#   1. `left` and `right` initialization: `left` must start at `i + 1` (not `0`).
#      Your check `left <= 0` was always True because `left = 0`, causing the 
#      loop to `continue` immediately on every iteration.
#   2. `nums[i] == nums[i-1]` check: Added `i > 0` condition to prevent checking 
#      out-of-bounds `nums[-1]` on the very first element.
#   3. Infinite loop when `total == 0`: If no duplicates existed, your code did 
#      not increment `left` or decrement `right`, creating an infinite loop.
#      You must always do `left += 1` and `right -= 1` after finding a triplet.
#   4. Values vs. Indices: You appended the indices `[left, right, i]`. The 
#      problem asks for the actual values `[nums[i], nums[left], nums[right]]`.
#   5. Early Return: Your `return res` was inside the `for` loop, which would 
#      exit after only examining the first element.
#
# Complexity Analysis:
#   - Time Complexity: O(n²) in ALL cases (not O(n)!). 
#     We iterate `n` times in the outer loop, and for each iteration, the two
#     pointers can scan up to `n` elements. Thus, O(n) * O(n) = O(n²).
#     Sorting takes O(n log n), which is dominated by O(n²).
#   - Space Complexity: O(1) or O(n) depending on the sorting implementation's 
#     auxiliary space (Python uses Timsort, which takes up to O(n) space).
# ============================================================


# ---- Tests ----
assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert threeSum([0, 1, 1]) == []
assert threeSum([0, 0, 0]) == [[0, 0, 0]]
assert threeSum([]) == []
assert threeSum([0]) == []
print("All tests passed!")
