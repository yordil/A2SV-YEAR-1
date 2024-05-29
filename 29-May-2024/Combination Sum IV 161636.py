# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        ans= 0
        path = []
        @cache
        def dp(tar):

            if tar == 0:
                return 1
            val = 0
            for n in nums:
                if tar - n >= 0:
                    val += dp(tar-n) 
                    
            return val

        return  dp(target)
        

            