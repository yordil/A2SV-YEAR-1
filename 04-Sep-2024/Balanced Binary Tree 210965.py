# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        flag = True

        def dfs(node):
            nonlocal flag
            if not node.left and not node.right:
                return 1

            l = 0
            r = 0

            if node.left:
                l = dfs(node.left )
            if node.right:
                r = dfs(node.right)
            flag = abs(l-r) <= 1 and flag
            return max(l , r) + 1

        dfs(root)

        return flag 