class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp(arr):

            dp = [0] * (len(nums)  +  1)

            for i in range(len(arr)):
                dp[i] = max(arr[i] + dp[i-2]  ,  dp[i-1])

            return max(dp)

        return max(dp(nums[1:]) , dp(nums[:-1]))