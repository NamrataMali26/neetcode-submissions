# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res =[]

        def dfs(curr):
            if not curr:
                return None
            
            left = dfs(curr.left)
            res.append(curr.val)
            right = dfs(curr.right)

        dfs(root)
        return res

        

        


    
        