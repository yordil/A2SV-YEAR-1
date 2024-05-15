# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        
        for i in range(len(prices)):
            
            if prices[i] - prices[l] < 0:
                l = i
            else:
                profit = max(profit , prices[i] - prices[l])
                
        return profit
                
          
            