# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque([root])
        direction  = 1
        ans = []
        while queue:
            current_level = []

            for i in range(len(queue)):

                node = queue.popleft()

                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                

            if direction:
                ans.append(current_level)
                direction ^=1
            else:
                ans.append(current_level[::-1])
                direction ^= 1
            
        
        return ans 






        # myhash = defaultdict(list)
        # count = 0
        # maxdepth = 0
        # tempans =[]

        # def helper(root , depth):
        #     nonlocal maxdepth
            
        #     if root:
        #         if not root.left and not root.right:
        #             myhash[depth].append(root.val)
        #             return depth
                    
        #         myhash[depth].append(root.val)
        #         maxdepth = helper(root.left ,  depth + 1)
        #         maxdepthright=helper(root.right ,depth + 1)
        #         return max(maxdepth,maxdepthright)
        #     return 0

        # maxx = helper(root , 0)

        # ans = []
        # sorted_dict = dict(sorted(myhash.items()))
        # print(myhash)
        # for key , val in sorted_dict.items():
        #     if key % 2 :
        #         ans.append(val[::-1])
        #     else:
        #         ans.append(val)

        # return ans
            
            # maxdepth =  max(maxdepth ,  1 + self.maxDepth(root.left))