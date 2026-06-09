class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(root):
            if not root:
                return [True,0]
            
            left = depth(root.left)
            right = depth(root.right)
            
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1],right[1])]
        
        return depth(root)[0]
