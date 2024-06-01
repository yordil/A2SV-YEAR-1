# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        def bfs():
            queue = deque([(root , 1)])
            answer = 1
            while queue:
                node , depth = queue.popleft()
                answer = max(depth , answer)
                for child in node.children:
                    queue.append((child  , depth+1))
                
            return answer
        
        return bfs()