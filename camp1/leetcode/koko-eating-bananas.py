class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return ceil(piles[0] / h )
        
        # piles.sort()
        left = 1
        right = max(piles)
        ans = right
        while left <= right:
            midd = (left + right) //2
            hours  = 0
            for i in range(len(piles)):
                hours += ceil(piles[i] / midd)

            if hours <= h:
                ans  = min(midd , ans)
                right = midd - 1
            else:
                left = midd + 1
        
        return ans
            