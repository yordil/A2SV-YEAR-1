# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        
        hashset  = set()
        counter = 1
        for i in s:
            if i in hashset:
                counter +=1
                hashset.clear()
            hashset.add(i)
        
        return counter
                