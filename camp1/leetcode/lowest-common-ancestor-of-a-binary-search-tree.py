# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = []
        ans2 = []
        r = root

        def helper(root , ans , node):
            if not root:
                return 
            ans.append(root)
            if node.val == root.val:
                return ans
            if root.val > node.val:
                return helper(root.left , ans , node)           
            elif root.val < node.val:
                # ans.append(root)
                return helper(root.right , ans , node)
            
            return ans

        print(p)
        a = helper(r , ans , p)
        b = helper(r , ans2, q)

        # print(a , b)
        lena = len(a)
        lenb = len(b)
        ptr1 , ptr2 = 0 , 0
        res = None
        while ptr1 < lena and ptr2 < lenb:
            if a[ptr1].val == b[ptr2].val:
                res = a[ptr1]
            else:
                break
            ptr1 +=1
            ptr2 +=1


        return res
