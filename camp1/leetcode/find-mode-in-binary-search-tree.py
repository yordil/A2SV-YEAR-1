# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
    
        def freq(count , roo):
            if not roo:
                return 
            
            count[roo.val] +=1
            freq(count , roo.right)
            freq(count , roo.left)
                
        count  = defaultdict(int)
        freq(count , root)
        maxx = max(count.values())

        ans = []

        for key , val in count.items():
            if val == maxx:
                ans.append(key)
        return ans
