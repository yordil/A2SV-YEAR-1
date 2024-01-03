from functools import reduce
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        Sum = 0
        operation = 0
        i=0
        seen={nums[0]}
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                operation+=len(nums)-i-1
            i+=1
        return operation
        
    
       
#        m = min(nums)
#        countidx = 0
#        i = 0

#        while i < len(nums):
#            countidx +=1
#            counter = 0
#            j = i+1
#            while nums[i] == nums[j] != m:
#                counter +=1
#                j+=1
            
#            operation += countidx * (counter)
            
#            i+=j
#        return operation

# 1 1  2    2  3   3  4
       




           