# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:    
        var = set(list(range(1 , len(nums)+1))) if len(nums) != 1 else set([1,2])
       
        sett = set(nums)

        diff = var - sett
        
        if sett == var:
            return len(nums) + 1
        return min(diff) if diff else len(nums)

        