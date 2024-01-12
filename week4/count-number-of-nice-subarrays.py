class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] = 1
            else:
                nums[i] = 0
        
        myhash = {0 : 1 }
        cursum = 0
        result = 0
        for n in nums:
            cursum +=n
            
            result += myhash.get(cursum - k, 0)
            myhash[cursum] = myhash.get(cursum , 0 ) + 1
            
        return result
                
        
                
        
                
            
            