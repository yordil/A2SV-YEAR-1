# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        indegree = [0] * n
        graph = defaultdict(list)

        for a , b in edges:
            graph[a].append(b)
            indegree[b] +=1
        
        if indegree.count(0) > 1:
            return -1
        else: return indegree.index(0)

