# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        
        
        def r(n):
            if n in dp:
                return dp[n]
            if n == 0:
                return nums[0]
            elif n == 1:
                return max(nums[0], nums[1])

            dp[n] = max(r(n-1), nums[n] + r(n-2))
            
            return dp[n]

        return r(len(nums)-1)