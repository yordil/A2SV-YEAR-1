# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        arr = []
        for a , b in zip(profits , capital):
            arr.append((b , a))
        arr.sort()
        total_capital = k
        j = 0
        while k:
            while j < len(arr)  and w >= arr[j][0]:
                heappush(heap , -(arr[j][1]))
                j+=1
            k-=1
            if heap:
                w += -heappop(heap)
        return w