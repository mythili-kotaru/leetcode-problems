# ============================================================
# 11. Container With Most Water
# ============================================================
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
#
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
#
# Example 1:
#   Input: height = [1,8,6,2,5,4,8,3,7]
#   Output: 49
#   Explanation: The vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
#   In this case, the max area of water the container can contain is 49.
#
# Example 2:
#   Input: height = [1,1]
#   Output: 1
#
# Constraints:
#   n == height.length
#   2 <= n <= 10^5
#   0 <= height[i] <= 10^4
# ============================================================


# ---- Solution: Two Pointers (Greedy contraction) ----
def maxArea(height: list[int]) -> int:
    """Return the maximum volume of water a container can hold."""
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Width between the two pointers
        width = right - left
        # Height is constrained by the shorter of the two lines
        h = min(height[left], height[right])
        # Calculate area and update the maximum
        current_water = width * h
        max_water = max(max_water, current_water)

        # Move the pointer pointing to the shorter vertical line.
        # Moving the pointer pointing to the longer line can never increase the area,
        # because the area is bounded by the shorter line, and the width decreases.
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# ============================================================
# Notes
# ============================================================
# Approach: Two Pointers
#   - We initialize two pointers: `left` at the start of the array and `right` at the end.
#   - At each step, we calculate the area formed by the vertical lines at these pointers.
#   - We always move the pointer corresponding to the shorter line inward.
#
# Mathematical Rationale (Why this is optimal):
#   - The area is defined as: Area = Width * min(height[left], height[right]).
#   - If we move the pointer with the larger height inward, the width decreases by 1, 
#     and the height can either decrease or stay the same (since it is still constrained 
#     by the original shorter side). Thus, the area is guaranteed to be smaller.
#   - To potentially find a larger area, we MUST move the pointer with the smaller height, 
#     as that is the only way we might find a taller bounding line that compensates for 
#     the decreased width.
#
# Complexity Analysis:
#   - Time Complexity: O(n)
#     The loop starts with pointers at both ends and contracts by 1 at each iteration.
#     Hence, we perform a single linear pass of the array.
#   - Space Complexity: O(1)
#     Only constant space is used for the `left`, `right`, and `max_water` variables.
# ============================================================


# ---- Tests ----
if __name__ == "__main__":
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert maxArea([1, 1]) == 1
    assert maxArea([4, 3, 2, 1, 4]) == 16
    assert maxArea([1, 2, 1]) == 2
    print("All tests passed!")
