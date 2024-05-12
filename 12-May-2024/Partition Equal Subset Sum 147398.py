# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)

        if summ % 2:
            return False
        halfsum = summ // 2

        @cache
        def dp(index, currsum):
            nonlocal halfsum
            if currsum > halfsum or index == len(nums):
                return False
            if currsum == halfsum:
                return True
            if dp(index + 1, currsum + nums[index]):
                return True
            if dp(index + 1, currsum):
                return True
            return False

        return dp(0, 0)
