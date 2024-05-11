# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1 )
        dp[0]  = 0
        for i in range(1 , amount+1):
            for coin in coins:
                if i - coin >=0:
                    dp[i]  = min(dp[i-coin] + 1 , dp[i])
       
        return dp[-1] if dp[-1] != float("inf") else -1
        # memo = {}
        # if amount == 0:
        #     return 0
    
        # def dp(currsum):
            
        #     val  = float("inf")
        #     if currsum in memo:
        #         return memo[currsum] 
                
        #     if currsum == 0:
        #         return 0

        #     if currsum < 0 :
        #         return float("inf")

        #     for idx in range(len(coins)):
        #         val = min(val , 1 + dp(currsum - coins[idx]))
    
        #     memo[currsum] = val
        #     return memo[currsum]    

        # r = dp(amount)   
         
        
        # return r if r != float("inf") else -1
        