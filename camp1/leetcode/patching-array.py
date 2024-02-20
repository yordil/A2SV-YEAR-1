class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        unreachable , answer = 1 , 0    
        i = 0
        N = len(nums)
        while unreachable <= n:
            if i < N and unreachable >= nums[i]:
                unreachable += nums[i]
                i+=1
            else:
                unreachable = (2 * unreachable) 
                answer +=1
        return answer