# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int: 
        
        Sum = sum(nums)
        targetvalue  = Sum - x
        if Sum == x: return len(nums)
        flag = -1 
        prefix = 0
        l = 0 
        
        for r in range(len(nums)):
            prefix += nums[r] 
            
            while prefix > targetvalue and l <= r:
                prefix -= nums[l]
                l +=1
                
                
            if prefix == targetvalue:
                flag = max(flag , r - l + 1)
            
        return -1 if flag == -1 else len(nums) - flag
            
            
        
            