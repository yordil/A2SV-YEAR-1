class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        
        summ = sum(nums)
        ontheGo  = 0
        N =  len(nums)
        
        ans = 0
        for i in range(N-1):
            ontheGo += nums[i]
            if ontheGo >= summ - ontheGo:
                ans +=1

        return ans 


        