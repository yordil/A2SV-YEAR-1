class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        
        requestp = [0] * len(nums)

        for start , end in requests:
            requestp[start] +=1
            if end < len(nums)-1:
                requestp[end+1] -=1
        
        requestp = list(accumulate(requestp))
        print(requestp)
        # map = Counter(requestp)
        maxsum = 0
        nums.sort()
        requestp.sort()
        
        for i in range(len(nums)):
            maxsum += (nums[i]*requestp[i])
        
        return maxsum %( 10**9+7)

        

        
