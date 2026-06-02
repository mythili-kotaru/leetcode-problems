from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(N * 2^N)
        - Sorting the array takes O(N log N).
        - In the worst case, we explore up to 2^N subsets.
        - Copying each valid subset into the result array takes O(N) time on average.
        
        Space Complexity: O(N)
        - O(N) auxiliary space for the recursion stack and the `comb` list.
        - (The output array `res` can take up to O(N * 2^N) space if all elements are unique).
        """
        res = []

        # Sort to easily skip duplicates
        nums.sort()
        
        def dfs(comb, i):
            if i >= len(nums):
                res.append(comb.copy())
                return
            
            # Include nums[i]
            comb.append(nums[i])
            dfs(comb, i + 1)
            comb.pop()

            # Skip duplicates for the "exclude" branch
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(comb, i + 1)

        dfs([], 0)
        return res
