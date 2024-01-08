class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        Sum , l = 0  , 0 
        length = inf
        
        for r in range(len(nums)):
            Sum += nums[r]
            while Sum >= target:
                Sum -= nums[l]                
                length = min(length , r-l + 1)
                l +=1
                
        return 0 if length == inf else length
