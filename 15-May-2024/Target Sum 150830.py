# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        ans = 0
        @cache
        def dp(idx , currsum):
            nonlocal ans 
            if idx == len(nums):
                if currsum == target:
                    return 1
                return 0
            return dp(idx+1 , currsum + nums[idx]) + dp(idx + 1 , currsum - nums[idx])

    
        return dp(0 , 0)