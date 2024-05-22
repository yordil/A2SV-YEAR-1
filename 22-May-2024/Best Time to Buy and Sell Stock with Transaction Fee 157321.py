# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        # @cache
        def dp(idx , lastbuy):
            if (idx , lastbuy) in memo:
                return memo[(idx , lastbuy)]
            if idx >=len(prices):
                return 0
            
            profit = prices[idx] - lastbuy - fee
            if  profit > 0:
                memo[(idx , lastbuy)] = max(dp(idx+1 , float("inf")) + profit  ,dp(idx+1 , lastbuy))
            else:
                lastbuy = min(prices[idx] , lastbuy)
                memo[(idx , lastbuy)]  = dp(idx+1 , lastbuy)
            return memo[(idx , lastbuy)]

        return dp(0 , float("inf"))
            