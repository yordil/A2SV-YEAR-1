class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        prefix = [0] * (len(nums ) + 1)

        for i in range(len(queries)):
            l , r = queries[i]
            prefix[l] +=1 
            prefix[r+1] -= 1
        
        prefix = list(accumulate(prefix))

        for i in range(len(nums)):
            nums[i] -= prefix[i]
            if nums[i] < 0:
                nums[i] = 0

        return len(set(nums)) == 1 and 0 in nums
             