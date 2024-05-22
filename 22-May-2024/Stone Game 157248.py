# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        totsum = sum(piles)
        @cache 
        def backtrack(start , end):
            if start == end:
                return 0
            

            takefirst = piles[start] + backtrack(start + 1 , end)  
            takeSecond = piles[end] +  backtrack(start  , end-1) 

            maxx = max(takefirst , takeSecond)

            return maxx

        ans =  backtrack(0 , len(piles) - 1)

        return True if ans >= ceil(totsum / 2 ) else False