# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []

        def helper( root , ans):
            if not root:
                return 
            helper(root.right , ans)
            ans.append(root.val)
            helper(root.left , ans)

            

        helper(root , ans)

        anss = 0

        ans.sort()

        for val in ans:
            if val >= low and val <= high:
                anss += val
            elif val > high:
                break
        return anss