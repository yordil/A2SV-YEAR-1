# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        Sum = 0
        largest = nums[len(nums) - 1]
        
        
        for i in range(k):
             Sum +=nums[len(nums) -1]
             nums[len(nums) - 1] +=1
            
        return Sum
             