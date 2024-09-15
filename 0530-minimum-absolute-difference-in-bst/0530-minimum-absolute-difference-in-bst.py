# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mindiff = float('inf')
        prev = None

        def dfs(node):
            nonlocal mindiff
            nonlocal prev
            if not node:
                return
            
            dfs(node.left)
            if prev is not None:
                mindiff = min(mindiff, node.val - prev)
            
            prev = node.val
            
            
            dfs(node.right)
        
        dfs(root)
       
        return mindiff
