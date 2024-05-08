# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modd = pow(10 , 9) + 7

        myans = []
        for i in range(n):
            myans.append( (efficiency[i]  , speed[i]))

        myans.sort(reverse = True)
        heap = []
        maxx = 0
        summ = 0
        for ef , sp in myans:
            summ += sp
            if len(heap) >= k:
                poped = heappop(heap)
                summ -= poped
            heappush(heap , sp)
            maxx = max(maxx , summ * ef)
        return maxx % modd
        





