# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # n SOLUTION BUT CHEAT HAH

        arr = []

        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        l , r  = 0 , len(arr) -1
        maxans = 0

        while l < r:
            maxans = max(maxans , arr[l] + arr[r])
            l+=1
            r-=1

        return maxans 
