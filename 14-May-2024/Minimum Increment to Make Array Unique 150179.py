# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                curr = nums[i-1] - nums[i]
                res += curr + 1
                nums[i] = nums[i-1] + 1
        return res
        