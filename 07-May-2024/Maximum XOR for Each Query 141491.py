# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        prefixXor = [0] * len(nums)
        prefixXor[0] = nums[0]
        maxx = pow(2 , maximumBit) - 1
        answer = []
        for i in range(1 , len(nums)):
            answer.append(prefixXor[i-1] ^ maxx) 
            prefixXor[i] = prefixXor[i-1] ^ nums[i]
        answer.append(prefixXor[-1] ^ maxx)
        return answer[::-1]
       