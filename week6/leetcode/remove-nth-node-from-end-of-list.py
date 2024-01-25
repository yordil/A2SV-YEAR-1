# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return 
        size = 0
        curr = head
        while curr:
            size +=1
            curr = curr.next
        needed_index = size - n
        if needed_index == 0:
            return head.next
        print(size)
        curr = head
        counter = 0
        while curr and curr.next:
            counter +=1
            print(counter)
            if counter == needed_index:
                curr.next = curr.next.next
                print(5)
                break
            
            curr = curr.next
    
            
        return head