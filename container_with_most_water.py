# ============================================================
# Container With Most Water
# ============================================================
# Given an integer array height of length n, find two lines that
# together with the x-axis form a container holding the most water.
# Return the maximum amount of water the container can store.
#
# Example 1: height = [1,8,6,2,5,4,8,3,7] → 49
# Example 2: height = [1,1]                → 1
# ============================================================


# ---- Solution: Two Pointers ----
def findContainer(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    maxVol = 0

    while left < right:
        vol = min(height[left], height[right]) * (right - left)  # BUG FIX: right-left, not right-left+1
                                                                  # width between indices i and j is j-i
        maxVol = max(maxVol, vol)

        # Move the shorter side inward — keeping the taller side
        # can only help (width shrinks regardless, so the only
        # chance to improve area is to find a taller wall)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxVol


# ============================================================
# Notes
# ============================================================
# Approach: Two Pointers (greedy)
#   - Start with the widest possible container (left=0, right=n-1).
#   - Area = min(height[left], height[right]) * (right - left)
#   - The bottleneck is always the shorter wall. Moving the taller
#     wall inward can never increase area (width shrinks AND height
#     stays bounded by the same short wall). So always move the
#     shorter wall — it's the only side that might improve.
#   - Repeat until pointers meet.
#
# Bug fix:
#   Width = right - left  (not right - left + 1)
#   Indices 1 and 8 are 7 units apart: 8 - 1 = 7, not 8.
#
# Complexity correction:
#   O(log n) is WRONG — O(log n) means the search space halves
#   each step (e.g. binary search). Here each step moves one
#   pointer by exactly 1, so we do at most n steps → O(n).
#
# Time Complexity:  O(n) — each pointer moves inward at most n times total
# Space Complexity: O(1) — only a few variables
# ============================================================


# ---- Tests ----
assert findContainer([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert findContainer([1, 1]) == 1
assert findContainer([4, 3, 2, 1, 4]) == 16   # symmetric, both 4s
assert findContainer([1, 2, 1]) == 2
assert findContainer([2, 3, 4, 5, 18, 17, 6]) == 17
print("All tests passed!")
