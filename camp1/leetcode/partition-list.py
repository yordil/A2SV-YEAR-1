# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0) 
        less_ = less
        greater = ListNode(0) 
        greater_ = greater
        
        curr = head
        while curr:
            if curr.val < x:
                less_.next = curr
                less_ = less_.next
            else:
                greater_.next = curr
                greater_ = greater_.next
            curr = curr.next
        
      
        less_.next = greater.next
        greater_.next = None 
        
        return less.next
