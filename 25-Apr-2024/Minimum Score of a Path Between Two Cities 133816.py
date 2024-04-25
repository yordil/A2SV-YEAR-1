# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        parent = {i: i for i in range(1 ,n+1)}
        size = {i: 0 for i in range(1 ,n+1)}

        def find(x):
            while x != parent[x]:
                x = parent[parent[x]]
            return x
        def union(x , y):
            parx = find(x)
            pary = find(y)
        
            if parx != pary:
                if  size[parx] > size[pary]:
                    parent[pary] = parx
                    size[parx] += pary
                else:
                    parent[parx] = pary
                    size[pary] += parx
        def isConnected(x , y):
            return find(x) == find(y)
        
        

        for fromm , to , dis in roads:
            union(fromm , to)

        minanswer = float('inf')
        for road in roads:
            x, y, distance = road
            if find(1) == find(x):
                minanswer = min(minanswer, distance)
        
        return minanswer
        
        