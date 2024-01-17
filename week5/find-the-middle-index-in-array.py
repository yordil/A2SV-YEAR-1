class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        right = 0
        for i in range(len(nums)):
            left += nums[i]

            right = total - left + nums[i]

            if left == right:
                return i
        return -1
         
            