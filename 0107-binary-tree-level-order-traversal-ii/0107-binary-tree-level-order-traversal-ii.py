# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []


        queue  = deque([root])
        ans  = []
        while queue:
            temp = []
            for i in range(len(queue)):

                node = queue.popleft()

                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            ans.append(temp)

        
        return ans[::-1]