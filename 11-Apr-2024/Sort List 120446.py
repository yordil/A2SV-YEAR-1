# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge_sort(head):
            if not head or not head.next:
                return head
    
    
            mid = find_middle(head)
            left_half = head
            right_half = mid.next
            mid.next = None
            
            
            left_sorted = merge_sort(left_half)
            right_sorted = merge_sort(right_half)
        

            return merge(left_sorted, right_sorted)

        def find_middle(head):
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(left, right):
            dummy = ListNode()
            current = dummy
            
            while left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next
            
        
            if left:
                current.next = left
            if right:
                current.next = right
            
            return dummy.next
        
        return merge_sort(head)
        
        

      
         
                    
