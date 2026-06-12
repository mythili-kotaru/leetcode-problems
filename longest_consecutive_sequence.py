from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a hash set for O(1) lookups
        num_set = set(nums)
        max_len = 0
        
        for n in num_set:
            # Check if this number is the start of a sequence
            if n - 1 not in num_set:
                start_num = n
                current_len = 1
                
                # Expand the sequence as long as the next number exists
                while start_num + 1 in num_set:
                    start_num += 1
                    current_len += 1
                    
                # Update the maximum length found so far
                max_len = max(max_len, current_len)
                
        return max_len

'''
Time Complexity: O(N)
- Where N is the length of the array `nums`.
- Although there is a nested while loop, it only runs for the start of a sequence. Every number is evaluated at most twice (once to check if it's the start, and once during the while loop sequence building). Thus, the overall time complexity is strictly linear, O(N).

Space Complexity: O(N)
- The hash set `num_set` requires O(N) space to store all the unique elements from the input array.
'''
