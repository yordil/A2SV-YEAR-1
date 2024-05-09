# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        sett =set()
        def c(n):
           
            if n == 1 or n == 2:
                sett.add(n)
                return n 
            if n not in dp:
                dp[n] = c(n-1) + c(n-2)
            
            return dp[n]

        
        return c(n)
            
