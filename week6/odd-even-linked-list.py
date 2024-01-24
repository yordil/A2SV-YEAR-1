# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            dummy = head

            even_head = head.next
            even = even_head
            odd = dummy

            while even and even.next and odd and odd.next:
                odd.next = odd.next.next
                even.next = even.next.next

                even = even.next
                odd = odd.next
            odd.next = even_head

            return dummy

