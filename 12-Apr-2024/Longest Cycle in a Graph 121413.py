# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        def dfs():
            maxx = -1
            visited = set()
            for i in range(len(edges)):
                lastconnected = {}
                count = 0
                curr = i
                lastconnected[edges[curr]] = count
                while edges[curr] not in visited and edges[curr] != -1:
                    count +=1
                    visited.add(edges[curr])
                    curr = edges[curr]
                    lastconnected[curr] = count

                if edges[curr] != -1 and edges[curr] in lastconnected:
                    maxx = max(maxx , count +1 - lastconnected[edges[curr]] )
            return -1 if maxx == 1 else maxx
    
        return dfs()
    
# '41 35 52 60'




            