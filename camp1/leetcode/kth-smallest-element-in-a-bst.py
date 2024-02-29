# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
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

        return ans[k-1]