# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        last_val = float('-inf')

        def helper(node):
            nonlocal last_val  

            if not node:
                return True
    
            if not helper(node.left):
                return False
          
            if node.val <= last_val:
                return False 
            last_val = node.val
    
            return helper(node.right)
        
        return helper(root)
