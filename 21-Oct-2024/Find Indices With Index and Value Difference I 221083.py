# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = [-1 , -1]
        if valueDifference == 0 and indexDifference == 0:
            return [0 , 0]
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i , j]
        
        return ans
