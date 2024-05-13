# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edgelist = defaultdict(set)
       
        for a , b  in edges:
            edgelist[a].add(b)
            edgelist[b].add(a)
           
        N = len(edges)
        
        for key , val in edgelist.items():
            if len(val) == N:
                return key
        return 0