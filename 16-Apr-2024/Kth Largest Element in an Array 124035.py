# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       
        # nums = [-i for i in nums]
        heap = []
        
        
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap , num)
            elif num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap , num)
            
        return heap[0]


        # nums = [-n for n in nums]
        # heapq.heapify(nums)
        # while k>1:
        #     nums[0] *=-1
        #     nums[-1] , nums[0] = nums[0] , nums[-1]
        #     heapq.heapify(nums)
        #     k-=1
      
        # return -nums[0]