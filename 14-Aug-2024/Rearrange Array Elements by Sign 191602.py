# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        length =  len(nums)
        positive_index  = 0 
        negative_index = 1
        
        result = [0] * length
        
        for i in nums:
            if i > 0:
                result[positive_index]  = i
                positive_index +=2
            else:
                result[negative_index] = i
                negative_index +=2
                
        return result
        