# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        dp = [0] * (n)
        dp[0] = 1
        p1 , p2 , p3 =  0 ,  0 ,  0 

        for i in range(1 , n):

            holder = min(dp[p1] * 2 , dp[p2] *  3, dp[p3] * 5 )
            dp[i] = holder


            if holder == dp[p1] * 2:
                p1 +=1
            if holder == dp[p2] * 3:
                p2 +=1
            if holder == dp[p3] * 5:
                p3 +=1
    
        return dp[-1]
          