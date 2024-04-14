# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:return []
        def bfs():
            que = deque([root])
            ans = []
         
            while que:
                a = len(que)
                
                currsum = 0
                for i in range(len(que)):
                    node = que.popleft()
                    currsum += node.val
                    
                    if node.right:
                        que.append(node.right)
                    if node.left:
                        que.append(node.left)
                
                ans.append(currsum/a)
            return ans 
        return bfs()
                