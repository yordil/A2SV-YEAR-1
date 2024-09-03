# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        answer = []

        if not root:
            return []


        def dfs(root , summ):
            nonlocal paths
            if not root.left and not root.right:
                if summ - root.val == 0:
                    paths.append(root.val)
                    answer.append(paths.copy())
                    print(answer)
                    paths.pop()
                   
                return False

            summ -= root.val

            paths.append(root.val)
    
            l = dfs(root.left , summ) if root.left else False

            r = dfs(root.right , summ) if root.right else False
            
            if paths:
                paths.pop()
            
        
        val = dfs(root , targetSum)

        return answer if answer else []
