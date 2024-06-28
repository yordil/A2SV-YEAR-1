# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
                
        parent = {i: i for i in range(n)}
        size = {i: 1 for i in range(n)}

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]  
                x = parent[x]
            return x

        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                if size[parentX] > size[parentY]:
                    parent[parentY] = parentX
                    size[parentX] += size[parentY]
                else:
                    parent[parentX] = parentY
                    size[parentY] += size[parentX]

        def isConnected(x, y):
            return find(x) == find(y)
                
        for a , b in edges:
            union(a , b)
        
        counter = defaultdict(int)

        for i in range(n):
            counter[find(i)] +=1
        vals = (counter.values())
        total = prod(vals)
        ANS =  0
        total_sum = sum(vals)
        tpro = sum(x * x for x in vals)
        ANS = (total_sum * total_sum - tpro) // 2
        return ANS

     