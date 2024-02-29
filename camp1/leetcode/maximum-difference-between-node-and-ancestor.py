# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    
        # ans = float("-inf")
        maxx = root.val
        minn = root.val

        def helper(root, maxx , minn):
            if not root:
                # ans = max(abs(minn - maxx)  , ans )
                # return max(abs(minn - maxx)  , ans )
                return maxx-minn

            
            maxx = max(root.val , maxx) 
            minn = min(root.val , minn)
           
            return max(helper(root.left , maxx, minn) ,  helper(root.right , maxx, minn) )

        return max(helper(root.left , maxx , minn ) , helper(root.right , maxx, minn))
        