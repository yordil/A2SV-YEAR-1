# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        prefixXor = [0] * len(nums)
        prefixXor[0] = nums[0]
        maxx = pow(2 , maximumBit) - 1
        for i in range(1 , len(nums)):
            prefixXor[i] = prefixXor[i-1] ^ nums[i]
       
        ans = [] 
        for i in range(len(nums)- 1 , -1 , -1):
            ans.append(prefixXor[i] ^ maxx)
        return ans