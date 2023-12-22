class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero = nums.count(0)
        ones = nums.count(1)
        ans = set()
        leftone = 0
        leftzero = 0
        rightone = 0
        maxzero = 0
        maxsum = 0
        for i in range(-1 , len(nums)):
            if i==-1:
                maxsum = ones
                ans.add(0)
                continue
                    
            if nums[i] == 0:
                leftzero +=1
            else:
                leftone += 1
                
            # leftzero = zero - leftone
            
            rightone = ones - leftone
            
            cursum = leftzero  + rightone
           
                
            if cursum  > maxsum:
                maxsum = max(maxsum , cursum)
                ans.clear()
                ans.add(i+1)
            
            if cursum == maxsum:
                ans.add(i+1)
                
        return list(ans)
            
                
                
            