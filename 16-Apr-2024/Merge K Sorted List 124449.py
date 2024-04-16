# Problem: Merge K Sorted List - https://leetcode.com/problems/merge-k-sorted-lists/

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
        for i in range(len(lists)):
            currlist = lists[i]
            while currlist:
                heap.append(currlist.val)
                currlist = currlist.next
        
        heapify(heap)
        if heap:
            dummy = ListNode(heappop(heap)) 
        else:
            return
        curr = dummy
        while heap:
            curr.next = ListNode(heappop(heap))
            curr = curr.next
          
        return dummy