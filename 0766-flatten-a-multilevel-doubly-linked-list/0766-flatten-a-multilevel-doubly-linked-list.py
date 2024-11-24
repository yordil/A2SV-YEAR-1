"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return 

        dummy = ListNode(0)

        stack = [head]

        curr = dummy

        while stack:

            
            node  = stack.pop()

            curr.next = node
            node.prev = curr
            curr = curr.next
            

            if node.next:
                stack.append(node.next)

            if node.child:
                stack.append(node.child)
                node.child = None

        dummy.next.prev = None 
        
        return dummy.next
        