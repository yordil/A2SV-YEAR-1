class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        n = len(prices)
        k = 2  
        dp = [[0] * (k + 1) for _ in range(n)]
        for t in range(1, k + 1):
            max_diff = -prices[0]
            for i in range(1, n):
                dp[i][t] = max(dp[i - 1][t], prices[i] + max_diff)
                max_diff = max(max_diff, dp[i - 1][t - 1] - prices[i])
        return dp[n - 1][k]