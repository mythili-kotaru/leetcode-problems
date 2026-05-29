# ============================================================
# 56. Merge Intervals
# ============================================================
# Given an array of intervals where intervals[i] = [start_i, end_i], 
# merge all overlapping intervals, and return an array of the 
# non-overlapping intervals that cover all the intervals in the input.
#
# Example 1:
#   Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#   Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
# Example 2:
#   Input: intervals = [[1,4],[4,5]]
#   Output: [[1,5]]
#   Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# Constraints:
#   1 <= intervals.length <= 10^4
#   intervals[i].length == 2
#   0 <= start_i <= end_i <= 10^4
# ============================================================


# ---- Solution: Sort and Merge ----
def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Merge all overlapping intervals and return the non-overlapping intervals."""
    if not intervals:
        return []

    # Sort intervals by their start time
    intervals.sort(key=lambda x: x[0])

    # Initialize results with the first interval
    res = [intervals[0]]

    for x, y in intervals[1:]:
        prev_end = res[-1][1]

        # If the current interval overlaps with the previous one, merge them
        if x <= prev_end:
            res[-1][1] = max(prev_end, y)
        else:
            # Otherwise, append the current interval as a new entry
            res.append([x, y])

    return res


# ============================================================
# Notes
# ============================================================
# Approach: Sorting & Greedy Linear Scan
#   - Sorting the intervals by their start coordinates is the core of this approach.
#     Once sorted, overlapping intervals are guaranteed to be adjacent.
#   - We initialize our list of merged intervals `res` with the first interval.
#   - We then iterate through the remaining intervals. For each interval `[x, y]`:
#     1. If the current interval's start `x` is less than or equal to the end of the 
#        last merged interval (`prev_end`), they overlap. We merge them by updating 
#        the end of the last merged interval to `max(prev_end, y)`.
#     2. If `x > prev_end`, they do not overlap. We append `[x, y]` to `res` as a 
#        new interval.
#
# Correctness Review:
#   - Your original solution was extremely clean, elegant, and 100% correct!
#   - We added a defensive `if not intervals: return []` check at the beginning, 
#     which is a great industry practice to prevent IndexError on empty lists.
#
# Complexity Analysis:
#   - Time Complexity: O(N log N)
#     Sorting the array of length N takes O(N log N) time.
#     The subsequent linear scan takes O(N) time since we process each interval exactly once.
#     Thus, the overall time complexity is dominated by the sort step: O(N log N).
#
#   - Space Complexity: O(N)
#     In Python, sorting (Timsort) can require up to O(N) auxiliary space in the worst case.
#     Additionally, the output list `res` stores the merged intervals, taking O(N) space.
# ============================================================


# ---- Tests ----
if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert merge([]) == []
    print("All tests passed!")
