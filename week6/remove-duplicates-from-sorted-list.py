# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr = head
            
            while curr.next and curr.next.next:

                a = curr.val
                b = curr.next.val

                if a == b :
                    curr.next = curr.next.next
                    continue
                    
                curr = curr.next
            if curr.next:
                if curr.val == curr.next.val:
                    curr.next = None

            
            return head


        return head