# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node, ans):
            if node is not None:
                postorder(node.left, ans)
                postorder(node.right, ans)
                ans.append(node.val)

        ans = []
        postorder(root, ans)
        return ans
