# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        heap = [- i for i in nums]

        heapify(heap)
        ans = 0
        while k:
            poped = heappop(heap)

            ans += abs(poped)
         
            heappush(heap , -ceil(abs(poped)/3))

            k-=1
        
        return ans