from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional['TreeNode']:
        if not preorder or not inorder:
            return None

        node = TreeNode(preorder[0])
        i = inorder.index(preorder[0])

        node.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        node.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
    
        return node

'''
Time Complexity: O(N^2)
- Where N is the total number of nodes in the tree.
- In the worst case (a skewed tree), `inorder.index()` takes O(N) time and is called N times, resulting in O(N^2) time complexity.
- For a perfectly balanced tree, the time complexity would be closer to O(N log N).

Space Complexity: O(N^2)
- Array slicing `preorder[...]` and `inorder[...]` creates new arrays at each recursive step. 
- In the worst case, this creates O(N^2) additional space.
- The recursion stack also uses O(N) space.
'''
