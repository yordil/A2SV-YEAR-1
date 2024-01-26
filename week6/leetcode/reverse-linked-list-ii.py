# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:    
        if not head:
            return
        if not head.next or left==right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev1 = dummy

        for _ in range(left-1):
            prev1 = prev1.next
        print(prev1)
        curr = prev1.next
        prev2 = None

        diff = (right - left) + 1
        for _ in range(diff):
            temp = curr.next
            curr.next = prev2
            prev2 = curr
            curr = temp 

        prev1.next.next = curr
        prev1.next = prev2
        # print("-----" , prev2)
        
        return dummy.next
           


    #     dummy = head
    #     leftcounter = 0
    #     rightcounter = 0
    #     prev1 = None
    #     curr = head
    #     final = None
    #     while leftcounter < left-1:
    #         prev1  =curr
    #         curr  = curr.next
    #         leftcounter +=1
    #     final = curr
    #     # print(final)
    #     # print(prev1.val)
    #     prev2 = None
    #     while diff:
           
    #     final.next = curr
    #     if prev1:
    #         prev1.next = prev2
    #     # prev2.next = final
    #     return dummy

    # #     dummy = head

    # #     leftcounter = 0
    # #     rightcounter = 0
    # #     curr = head
    # #     prev1 = None
    
        

    #     while leftcounter < left-1:
    #         prev1  =curr
    #         curr  = curr.next
    #         leftcounter +=1
    #     # print(prev1)
    #     node2 = prev1.next
    #     prev2 = None
    #     # print(curr)
    #     # print(node2)
    #     # prev2.next = curr
    #     node2.next = curr
    #     prev1.next = prev2
    #     # prev1.next = curr

    #     return dummy
    

    # # prev , curr = None , head
    # # while leftcounter < left-1:
    # #     leftcounter +=1
    # #     prev = curr
    # #     curr = curr.next
    