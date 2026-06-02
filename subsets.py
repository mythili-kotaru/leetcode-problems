from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(N * 2^N)
        - N is the number of elements in `nums`.
        - There are 2^N possible subsets.
        - Copying each subset takes O(N) time in the worst case.
        
        Space Complexity: O(N)
        - O(N) auxiliary space for the recursion stack and the `comb` list.
        - (Note: The output array `res` requires O(N * 2^N) space).
        """
        res = []
        n = len(nums)

        def dfs(comb, i):
            if i >= n:
                res.append(comb.copy())
                return

            # Include nums[i]
            comb.append(nums[i])
            dfs(comb, i + 1) 
            
            # Exclude nums[i]
            comb.pop()
            dfs(comb, i + 1) 
        
        dfs([], 0) 
        return res
