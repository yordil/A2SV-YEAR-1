# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxx = 0
        for num in nums:
            maxx |= num
        
    
        def backtrack(idx: int, curr: int) -> int:
            
            if idx == len(nums):
                
                return 1 if curr == maxx else 0
            
            
            ic = backtrack(idx + 1, curr | nums[idx])
            
            
            ex = backtrack(idx + 1, curr)
            
        
            return ic + ex
        
        
        return backtrack(0, 0)
