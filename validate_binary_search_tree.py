# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        """
        Determines if a binary tree is a valid Binary Search Tree (BST).
        
        Solution Explanation (Recursive Depth-First Search):
        - A valid BST requires that all nodes in the left subtree are strictly less than the node's value,
          and all nodes in the right subtree are strictly greater.
        - We use a helper function `validateBST` that takes the current node and the valid range `(left, right)`.
        - For the root node, the range is `(-inf, inf)`.
        - When we go left, the upper bound becomes the current node's value.
        - When we go right, the lower bound becomes the current node's value.
        - If a node's value falls outside the `(left, right)` range, it's not a valid BST.
        
        Time Complexity: O(N)
        Where N is the number of nodes in the tree. In the worst case, we must visit every node once.
        
        Space Complexity: O(H)
        Where H is the height of the tree. This is the space required for the call stack during the recursive DFS.
        In the worst case (a skewed tree), this is O(N). In a balanced tree, this is O(log N).
        """
        def validateBST(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return (validateBST(node.left, left, node.val) and 
                    validateBST(node.right, node.val, right))

        return validateBST(root, float('-inf'), float('inf'))
