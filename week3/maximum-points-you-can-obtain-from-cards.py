class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        total = sum(cardPoints)   #O(N)
        
        Max = -1
        cursum = 0
        n = len(cardPoints)
        
        windowsum = 0
        windowsize = n-k
        
        for i in range(n):
            
            windowsum += cardPoints[i]
            
            if i - windowsize >=0:
                windowsum -= cardPoints[i-windowsize]
                
            if i >= windowsize - 1:
                Max = max(Max , total-windowsum)
                
        return Max
                