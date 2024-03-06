class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left  , right = max(weights)  , sum(weights)
        tempsum = 0
     
        while left < right:  
            midd = (left + right) // 2
            currsum = 0
            day = 1
            for w in weights:
                if currsum + w > midd:
                    currsum = 0
                    day += 1
                currsum +=w
         
            if day > days:
                left  = midd + 1
            else:
                right = midd 
            # else:
            #     return midd
            

        return left

