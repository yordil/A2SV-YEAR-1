# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        

        answer = []
        
        
        def dfs(curr , path , val):
            
            if not curr:
                return []

            if curr.val ==  val:
                return path

        
            
            path.append("L")
            result = dfs(curr.left ,path ,  val)
            if result:
                return path
            path.pop()
        
            path.append("R")
            result = dfs(curr.right ,path , val)

            if result:
                return result
                
            path.pop()
            



        firstpath = dfs(root , [] , startValue)
        secondpath = dfs(root , [] , destValue)
        minlen = min(len(firstpath) , len(secondpath))
        i = 0
        print(firstpath , secondpath)
        while i < minlen and firstpath[i] == secondpath[i]:
            i+=1
        
        ans  = "U" * len(firstpath[i:]) + "".join(secondpath[i:])

        return ans 

