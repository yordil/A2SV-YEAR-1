# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        Sum = sum(nums)
        
        prefix = 0
        
        rightsum = 0 
        for i in range(len(nums)):
            prefix +=nums[i]
            rightsum = Sum - prefix + nums[i]
            
            if(prefix == rightsum):
                return i
            
         
            
        return -1
    
    