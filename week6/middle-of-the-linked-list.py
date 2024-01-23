# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        sl , fast = head , head
        
        while fast and fast.next:
            sl = sl.next
            
            fast = fast.next.next
            
        return sl