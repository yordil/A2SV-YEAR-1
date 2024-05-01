# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        fx = nums[0]
        
        for i in nums[1:]: fx =  fx ^ i
        print(fx)
        
        return bin(fx^k).count("1")