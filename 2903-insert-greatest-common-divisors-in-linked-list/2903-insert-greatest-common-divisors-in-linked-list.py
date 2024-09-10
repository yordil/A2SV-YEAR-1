# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head

        while curr and curr.next:

            gc = gcd(curr.val , curr.next.val)

            gcval = ListNode(gc)

            gcval.next = curr.next
            curr.next = gcval

            curr = gcval.next

          
        return head
