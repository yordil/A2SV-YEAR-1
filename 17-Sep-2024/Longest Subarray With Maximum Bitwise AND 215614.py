# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1

        l ,r  = 0 , 1
        maxx = max(nums)
        count = 0
        while l < len(nums):
            r = l
            p = l
            while r < len(nums) and nums[r] == maxx:
                l =r
                r+=1
                count = max(count , r - p )
            
                
            l+=1

        return count
