# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        dummy = ListNode()
        dummy.next = head
        curr = dummy.next
        arr = []
        while curr:
            size += 1
            curr = curr.next

        quotient, remainder = size // k  , size % k

        curr = dummy.next
        length = 0
        for i in range(k):
            if i < remainder :
                length = quotient + 1
            else:
                length = quotient

            if not length:
                arr.append(None)
            else:
                arr.append(curr)
                for _ in range(length - 1):
                    curr = curr.next
                temp = curr.next
                curr.next = None
                curr = temp

        return arr
