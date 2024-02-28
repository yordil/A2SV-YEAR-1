# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        maxdepth = 0
        if root:
            maxdepth = 1 + self.maxDepth(root.right)
            maxdepth =  max(maxdepth ,  1 + self.maxDepth(root.left))
        return maxdepth
            