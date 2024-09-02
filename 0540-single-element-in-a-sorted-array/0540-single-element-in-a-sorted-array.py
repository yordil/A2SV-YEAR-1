class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left , right  = 0  , len(nums) - 1 
        nums.append(-1)
        while left <= right:

            midd = (left +  right) // 2 

            # check if i am not in disrupted place
            if midd % 2 == 0 and nums[midd  + 1 ] == nums[midd]:
                left = midd + 1
        
            elif midd % 2 == 1 and nums[midd - 1 ] == nums[midd]:
                left = midd + 1
            else:
                right = midd - 1
        
        return nums[left]