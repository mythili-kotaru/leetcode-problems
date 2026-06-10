from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []
            
        queue = deque([root])
        res = []

        while queue:
            lis = []
            for _ in range(len(queue)):
            
                elem = queue.popleft()
                lis.append(elem.val)

                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)

            res.append(lis)
        return res

'''
Time Complexity: O(N)
- Where N is the total number of nodes in the binary tree. 
- We visit each node exactly once during the BFS traversal.

Space Complexity: O(N)
- In the worst case (a perfectly balanced tree), the maximum number of nodes in the queue is at the last level, which is roughly N/2. 
- Therefore, the space complexity is O(N) to hold the nodes in the queue, plus O(N) to store the result list `res`.
'''
