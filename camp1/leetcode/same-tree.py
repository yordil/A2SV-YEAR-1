# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # while p.left and q.left:
        #     if p.val != q.val:
        #         return False
        # while p.right != q.right:
        #     if p.val != q.val:
        #         return False
        # return True
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
             return self.isSameTree(p.right , q.right) & self.isSameTree(p.left , q.left)
             
            
            

        return False

        # P= p
        # Q =q

        # if P and Q:
        #     if P and Q:
        #         a =  self.isSameTree(P.right , Q.right)
        #         print(P.val , Q.val)
        #         if P.val != Q.val:
        #             print(P.val , Q.val)
        #             return False
        #     elif  P and Q:
        #         a = self.isSameTree(P.left , Q.left)
        #         print(P.val , Q.val)
        #         if P.val != Q.val:
        #             return False
        # if not P and Q:
        #     return False
        # if not Q and P:
        #     return False
       
        # return True
            
            
        