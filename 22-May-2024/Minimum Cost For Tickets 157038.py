# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def dp(idx):

            if idx >= len(days):
                return 0
            cost = float("inf")
            for i , val in enumerate([1 , 7 , 30]):
                index  = bisect_left(days , val + days[idx])
                cost = min(cost , dp(index)+costs[i])
            return cost
        return dp(0)
