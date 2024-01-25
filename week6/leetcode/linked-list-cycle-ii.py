# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        curr = None
        slow = head
        fast = head
        
        while fast and  fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                print(slow)
                curr = slow
                break

        starthead = head
        if not curr:
            return 
        while starthead.next and curr.next:
            if starthead == curr:
                return curr
            curr = curr.next
            starthead = starthead.next


        return curr




