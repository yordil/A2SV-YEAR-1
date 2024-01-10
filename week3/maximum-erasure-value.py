class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashset = set()
        Sum = 0
        maxsum = -inf
        left = 0
        for i in range(len(nums)):
            while nums[i] in hashset:
                Sum -= nums[left]
                hashset.discard(nums[left])
                left+=1
            hashset.add(nums[i])
            Sum += nums[i]
            
            maxsum = max(maxsum , Sum)
            
        return maxsum
            
            
                