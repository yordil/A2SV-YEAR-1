class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        '''
        THE CONSTRANINT IS SMALL AND BRUTEFORCE WILL PASS
        '''
    
        count = 0
        
        for i in range(len(nums)-1):
            for j in range(i+1 , len(nums)):
                if (i*j) % k == 0 and nums[i] == nums[j]:
                    
                    count+=1
                    
        return count