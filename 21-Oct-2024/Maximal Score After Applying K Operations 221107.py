# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

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