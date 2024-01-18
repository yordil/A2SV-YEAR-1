class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        counter = 0
        
        Hash = { 0 : 1}
        
        Sum = 0
        
        
        for i in range (len(nums)):
            Sum += nums[i]
            
            mod = Sum % k
            
            counter += Hash.get(mod , 0)
            
            Hash[mod] = Hash.get(mod , 0) + 1
            
        return counter
             
            
            