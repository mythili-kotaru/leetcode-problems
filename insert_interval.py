# ============================================================
# 57. Insert Interval
# ============================================================
# You are given an array of non-overlapping intervals where 
# intervals[i] = [start_i, end_i] represent the start and the end of the 
# ith interval and intervals is sorted in ascending order by start_i. 
# You are also given an interval newInterval = [start, end] that represents 
# the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in 
# ascending order by start_i and intervals still does not have any 
# overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# Example 1:
#   Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#   Output: [[1,5],[6,9]]
#
# Example 2:
#   Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#   Output: [[1,2],[3,10],[12,16]]
#   Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
# Constraints:
#   0 <= intervals.length <= 10^4
#   intervals[i].length == 2
#   0 <= start_i <= end_i <= 10^5
#   intervals is sorted by start_i in ascending order.
#   newInterval.length == 2
#   0 <= start <= end <= 10^5
# ============================================================


# ---- Solution: One-Pass Linear Insertion & Merge ----
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    """Insert newInterval into sorted intervals, merging overlaps along the way."""
    res = []

    for i in range(len(intervals)):
        # Case 1: Current interval is completely to the left of newInterval
        if intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
        
        # Case 2: Current interval is completely to the right of newInterval
        # We can append newInterval, extend with the rest of the list, and exit early!
        elif intervals[i][0] > newInterval[1]:
            res.append(newInterval)
            res.extend(intervals[i:])
            return res
        
        # Case 3: Overlap occurs, merge current interval into newInterval
        else:
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1]),
            ]
            
    # Append the last merged/inserted interval
    res.append(newInterval)
    return res


# ============================================================
# Notes
# ============================================================
# Approach: One-Pass Linear Scan
#   - Since `intervals` is already sorted, we can complete the insert and merge 
#     in a single linear scan:
#     1. If the current interval ends before `newInterval` starts, it cannot 
#        overlap. We append it to `res`.
#     2. If the current interval starts after `newInterval` ends, there are 
#        no more overlaps possible. We append `newInterval`, extend the list 
#        with all remaining intervals, and return immediately.
#     3. If there is an overlap, we merge them by updating `newInterval`'s bounds 
#        to: `[min(interval.start, new.start), max(interval.end, new.end)]`.
#
# Correctness Review:
#   - Your original solution is absolutely brilliant, clean, and 100% correct!
#   - The logic handles all boundary cases (inserting at start, middle, end, or into 
#     an empty array) perfectly without needing special branching.
#
# Complexity Analysis:
#   - Time Complexity: O(N)
#     We iterate through the intervals at most once. The early return and `res.extend` 
#     operation also run in linear time.
#   - Space Complexity: O(N)
#     We allocate a new list `res` to hold the output, which takes space proportional 
#     to the input length. Auxiliary space is O(1) if we exclude the return list.
# ============================================================


# ---- Tests ----
if __name__ == "__main__":
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16],
    ]
    # Edge case: Empty intervals list
    assert insert([], [5, 7]) == [[5, 7]]
    # Edge case: Insert at the very beginning
    assert insert([[3, 5]], [1, 2]) == [[1, 2], [3, 5]]
    # Edge case: Insert at the very end
    assert insert([[1, 2]], [3, 4]) == [[1, 2], [3, 4]]
    print("All tests passed!")
