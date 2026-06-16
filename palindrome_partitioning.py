from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(word):
            left, right = 0, len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(i, comb):
            # Base case: we've successfully partitioned the whole string
            if i == len(s):
                res.append(list(comb))
                return
            
            for j in range(i, len(s)):
                subst = s[i : j + 1]

                if isPalindrome(subst):
                    comb.append(subst)
                    dfs(j + 1, comb)
                    comb.pop() # Backtrack

        dfs(0, [])
        return res

'''
Time Complexity: O(N * 2^N)
- Where N is the length of string `s`. 
- In the worst case (e.g. all identical characters like "aaaa"), there are 2^(N-1) possible partitions. 
- For each valid partition, we might take O(N) time to copy the combination to the result list and verify palindromes.

Space Complexity: O(N)
- This is the space used by the recursion stack and the `comb` list. 
- The depth of the recursion tree can go up to N in the worst case. 
- (Note: This space complexity excludes the space required to store the output list `res`).
'''
