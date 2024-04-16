# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        cc = Counter(nums)
        heap = []
        for key ,  val in cc.items():
            if len(heap) < k:
                heapq.heappush(heap ,(val , key))
            elif val > heap[0][0]: 
                heapq.heappop(heap)
                heapq.heappush(heap , (val , key))
    
        return [i[1] for i in heap]

        