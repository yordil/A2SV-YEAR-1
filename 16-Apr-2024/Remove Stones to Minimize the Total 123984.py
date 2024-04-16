# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

from sortedcontainers import SortedList, SortedSet, SortedDict 
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        aa = SortedList(piles)
        while k:
            val = aa.pop()
            aa.add(ceil(val/2))
            k-=1
       
        return sum(aa)
