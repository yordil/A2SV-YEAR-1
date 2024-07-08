# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        first  = head.next
        
        while first and first.next:
            tempsum = 0
            curr = first
            while first and first.next and first.val !=0:
                tempsum += first.val
                first = first.next
            curr.val = tempsum
            curr.next = first.next
            first = first.next
         
        return head.next