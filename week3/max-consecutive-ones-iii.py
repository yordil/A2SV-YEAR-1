class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxval = 0
        for r , num in enumerate(nums):
            k -=1 - num
            
            if k < 0:
                k += 1 - nums[left]
                left +=1
            else:
                maxval = max(maxval , r-left+1)
             
        return maxval
    
    
    
    
    
    
    
    
  