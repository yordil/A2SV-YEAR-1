class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # arra = []
        # arrb = []
        ans=0
        costs.sort(key = lambda x : (x[1]- x[0]))
        for i in range(len(costs)//2):
            ans += costs[i][1]
        for i in range(len(costs)//2 , len(costs)):
            ans += costs[i][0]

        return ans