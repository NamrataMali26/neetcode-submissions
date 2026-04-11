# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curr_sum =0
        if not root:
            return False
        def dfs(curr, curr_sum):
            if not curr:
                return False
            curr_sum += curr.val
            left = curr.left
            right = curr.right
            if not curr.left and not curr.right:
                return curr_sum == targetSum
            return dfs(left, curr_sum) or dfs(right, curr_sum)

        return dfs(root, curr_sum)
        