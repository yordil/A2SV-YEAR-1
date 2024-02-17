# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        dummy1 = ListNode()
        dummy1.next = headA
        dummy2 = ListNode()
        dummy2.next = headB
        curr = dummy1.next
        curr2 = dummy2.next
        # myset = set()
        len1 , len2 = 0 , 0
        while curr and curr.next:
            curr = curr.next
            len1+=1
            
        while curr2 and curr2.next:
            curr2 = curr2.next
            len2 +=1
        
        curr = dummy1.next
        curr2 = dummy2.next


        if len2 >= len1:
            diff = len2-len1
            while diff:
                curr2 = curr2.next
            
                diff -=1

            while curr:
                if curr == curr2:
                    return curr
                curr = curr.next
                curr2 = curr2.next

        elif len1 > len2:
            diff = len1-len2
            while diff:
                curr = curr.next
                diff -=1

            while curr2:
                if curr == curr2:
                    return curr
                curr = curr.next
                curr2 = curr2.next
        
        return 





        # dummy1 = ListNode()
        # dummy1.next = headA
        # dummy2 = ListNode()
        # dummy2.next = headB
        # curr = dummy1
        # curr2 = dummy2
        # myset = set()


        # while curr and curr.next:
        #     curr = curr.next
        #     myset.add(curr)
        # while curr2 and curr2.next:
        #     curr2 = curr2.next
        #     if curr2 in myset:
        #         return curr2
        # return 

# How can I do this O(1) space bro it is preety easy in O(N) 
