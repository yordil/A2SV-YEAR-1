# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(r , answer):
            if not r: return 0

            answer = answer * 10 
            answer += (r.val)
            if not r.left and not r.right:
                return answer
            
            return helper(r.left , answer) + helper(r.right , answer)
            
        
        return helper(root , 0)
