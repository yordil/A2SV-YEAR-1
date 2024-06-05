# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        fast , slow  = head , head 
        curr = None 
      
        while fast and fast.next:
            fast = fast.next.next
            nextnode = slow.next
            slow.next = curr
            curr = slow
            slow = nextnode
    
        firsthalf = curr
        secondhalf = slow
        maxsum = 0
        while firsthalf:
            maxsum = max(maxsum , firsthalf.val + secondhalf.val)
            secondhalf = secondhalf.next
            firsthalf = firsthalf.next
        return maxsum



        





        # n SOLUTION BUT CHEAT HAH
        # space O(N) => 

        # arr = []

        # curr = head
        # length = 0
        # while curr:
        #     arr.append(curr.val)
        #     curr = curr.next
        #     length +=1
        
        # curr = head
        # curr2 = head
        # while curr:
            

        
        # l , r  = 0 , len(arr) -1
        # maxans = 0

        # while l < r:
        #     maxans = max(maxans , arr[l] + arr[r])
        #     l+=1
        #     r-=1

        # return maxans 


