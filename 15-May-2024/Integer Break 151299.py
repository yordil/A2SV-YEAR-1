# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n -1
       
        @cache
        def dp(score):
            x = 0
            if score < 0:
                return 0
            if score < 4 :
                return score


            for i in range(2 , score+1):
                x = max(x,dp(score-i)*i )
                
            return x
        return dp(n)
            

            
