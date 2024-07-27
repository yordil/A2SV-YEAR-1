# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        left , right = 0 , 1
        
        while right < len(nums):  
            
            if nums[left] == nums[right]:
                nums[left] *= 2
                nums[right] *= 0
                
            left +=1
            right+=1
        
        l = 0
        for r in range(len(nums)): 
            
            if nums[r]:
                nums[l] , nums[r] = nums[r] , nums[l]
                
                l +=1
                
        return nums
            