# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

from sortedcontainers import SortedList
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        aa = SortedList(piles)
        print(aa[-1])
        while k:
            val = aa.pop()
            aa[-1] = ceil(aa[-1]/2)
            k-=1
       
        return sum(aa)
