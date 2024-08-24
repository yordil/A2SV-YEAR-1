# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        if not lists:
            return
        ptr = 0
        for i in range(len(lists)):
            currlist = lists[i]
            if currlist:
                heap.append((currlist.val , ptr , currlist.next))
                ptr+=1
        heapify(heap)
        dummy = ListNode()
        curr = dummy
        while heap:
            value , flag , currnode = heappop(heap)
            curr.next = ListNode(value)
            curr = curr.next

            if currnode:
                heappush(heap , (currnode.val , flag , currnode.next))
        
        return dummy.next
    