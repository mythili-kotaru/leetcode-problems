from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_idx = 0
        total_gas = 0
        current_gas = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_gas += diff
            current_gas += diff

            # If current gas dips below 0, we can't reach the next station from any 
            # station between start_idx and i. So we must start at i + 1.
            if current_gas < 0:
                start_idx = i + 1
                current_gas = 0
                
        # If total gas across the whole trip is >= 0, a solution is guaranteed to exist.
        return start_idx if total_gas >= 0 else -1

'''
Time Complexity: O(N)
- Where N is the number of gas stations. We iterate through the `gas` and `cost` arrays exactly once in a single pass.

Space Complexity: O(1)
- We only use a few integer variables (`start_idx`, `total_gas`, `current_gas`) to keep track of the running totals and starting position, which requires constant extra space.
'''
