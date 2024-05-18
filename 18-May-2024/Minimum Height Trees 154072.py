# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  
        
        edge = defaultdict(list)
        for u, v in edges:
            edge[u].append(v)
            edge[v].append(u)
        
        
        ll = [node for node in range(n) if len(edge[node]) == 1]
        remaining_nodes = n
        while remaining_nodes > 2:
            neww = []
            for leaf in ll:
                neighbor = edge[leaf].pop()  
                edge[neighbor].remove(leaf)
                if len(edge[neighbor]) == 1:
                    neww.append(neighbor)
                remaining_nodes -= 1
            ll = neww
        
        return ll