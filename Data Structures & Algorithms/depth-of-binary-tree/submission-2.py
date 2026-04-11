# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(curr):
            if not curr:
                return 0
            
            left = curr.left
            right = curr.right
            return 1 + max(dfs(left), dfs(right))

        return dfs(root)
        