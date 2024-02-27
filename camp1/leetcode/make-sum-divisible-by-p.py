class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        remainder = sum(nums)%p
        if remainder == 0:
            return 0
        if sum(nums) < p:
            return -1
        ans = len(nums)
        pre = 0
        di = {0:-1}
      
        for i in range(len(nums)):
            pre += nums[i]
            mod = ((pre%p) - remainder) %p
            if mod in di:
                ans = min(ans,i-di[mod])
            
            di[pre % p] = i
   
        return ans if ans != len(nums) else -1