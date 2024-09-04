# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        parent = defaultdict(TreeNode)
        answer = []
        def find_path(curr):
            path =[ str(curr.val)]
            while curr in parent:
                curr = parent[curr]
                path.append("->")
               
                path.append(str(curr.val ))
              
            answer.append("".join(path[::-1]))
                
        def dfs(curr):

            if not curr.left and not curr.right:
                find_path(curr)

            if curr.left:
                parent[curr.left] = curr
                dfs(curr.left)
            if curr.right:
                parent[curr.right] = curr
                dfs(curr.right)
            

        
        dfs(root)

        return answer
        
        
