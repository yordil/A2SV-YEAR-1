# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        r= root
        ans = []
        def helper(root , ans):
            if not root:
                return 
            helper(root.left , ans)
            ans.append(root.val)
            helper(root.right , ans)
            
            return ans

        helper(root , ans)
    
        for i in range(1 , len(ans)):
            if ans[i-1] >= ans[i]:
                return False

        return True 