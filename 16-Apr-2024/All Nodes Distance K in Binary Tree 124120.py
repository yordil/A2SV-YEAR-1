# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        myhash = defaultdict(list)

        def build(node):
            if node.left:
                myhash[node.val].append(node.left.val)
                myhash[node.left.val].append(node.val)
                build(node.left)

            if node.right:
                myhash[node.val].append(node.right.val)
                myhash[node.right.val].append(node.val)
                build(node.right)

        build(root)

        visited = set()
        que = deque([(target.val,0)])
        visited.add(target.val)
        ans = []
        while que:
            node , lenn = que.popleft()
            if lenn == k:
                ans.append(node)

            for neighbour in myhash[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    que.append((neighbour,lenn + 1))
        return ans


        
        