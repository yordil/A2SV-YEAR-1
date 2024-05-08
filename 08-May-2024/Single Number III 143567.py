# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        finalxor = nums[0]
        for i in nums[1:]:
            finalxor ^= i
        
        setted , unsetted = 0 , 0
        finalbit = 0
        for i in range(31):
            if finalxor & 1<<i:
                finalbit = i
                break
        for num in nums:
            if num & 1<<finalbit:
                setted ^=num
            else:
                unsetted ^=num

        return [setted , unsetted]