# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head:
            lis = []

            curr = head

            while curr:
                lis.append(curr.val)
                curr= curr.next
        
        

            return lis == lis[::-1]
           
        return True