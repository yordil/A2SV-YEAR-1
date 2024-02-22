class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        op = 0
        last = nums[-1]

        for i in range(len(nums)-2 , -1 , -1):
            curr = 0
            if nums[i] > last:
                currop = ceil(nums[i] / last)
                op += currop -1 
                last = floor(nums[i]/ currop)
            else:
                last = nums[i]
                    
        return op

