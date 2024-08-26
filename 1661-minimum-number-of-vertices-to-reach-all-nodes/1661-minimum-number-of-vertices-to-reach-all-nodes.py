class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        
        inc = collections.defaultdict(list)
        
        for s , d in edges:
            inc[d].append(s)
            
        r = []
        
        for i in range(n):
            if not inc[i]:
                r.append(i)
                
        return r