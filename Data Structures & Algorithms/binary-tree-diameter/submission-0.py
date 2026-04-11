# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = [0]
        def dfs(curr):
            if not curr:
                return 0
            
            left_max = dfs(curr.left)
            right_max = dfs(curr.right)
            res[0] = max(res[0], left_max + right_max)
            return 1 + max(left_max, right_max)

        dfs(root)
        return res[0]
        