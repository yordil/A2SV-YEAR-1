# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        inf = float("inf")
        totalprofit = 0
        N = len(difficulty)
        diffprofit = []
        for d , p in zip(difficulty, profit):
            diffprofit.append((d, p))
        diffprofit.sort()
        # reorder it 
        newprofit  = []
        maxx = 0
        
        for d , p in diffprofit:
            maxx = max(maxx , p)
            newprofit.append((d , maxx))

        
        for i in range(len(worker)):
            index = bisect_right(newprofit ,(worker[i] , inf))
            if index < N and  worker[i] == newprofit[index][0]:
                totalprofit += newprofit[index][1]
            elif index < N and worker[i] < newprofit[index][0] and index != 0:
                totalprofit += newprofit[index-1][1]
            elif index == N:
                totalprofit += newprofit[index-1][1]
        
        return totalprofit

        # O(N*M) 
        #       for w in worker:
        #     j = 0
        #     maxprofit = 0
        #     maxpower = w
        #     minpower = 1
        #     while maxpower <= minpower:
        #         mid = (maxpower + minpower) // 2
        #     while j < len(diffprofit) and diffprofit[j][0] <= w:
        #         maxprofit = max(maxprofit, diffprofit[j][1]) 
        #         j += 1
        #     totalprofit += maxprofit  
        
        # return totalprofit
       
