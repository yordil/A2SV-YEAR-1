# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        dp = [0] * (amount + 1)
        dp[0] = 1
        counter =  0
        for c in coins:
            for i in range(1, amount+1):
                if i - c >=0:
                    dp[i] +=dp[i-c]  
                    counter+=1

        return dp[-1]
        
        


        # counter = 0
        # memo = {}
        # def dp(currsum):
        #     nonlocal counter
        #     val  = float("inf")
        #     if currsum in memo:
        #         return memo[currsum] 
                
        #     if currsum == 0:
        #         return counter + 1

        #     if currsum < 0 :
        #         return float("inf")

        #     for idx in range(len(coins)):
        #         val = min(val , 1 + dp(currsum - coins[idx]))
    
        #     memo[currsum] = counter
            
        # r = dp(amount)   
        
        # return r if r != float("inf") else -1

