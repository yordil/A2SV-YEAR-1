# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        for _from , to in edges:
            graph[to].append(_from)
           
        ans = [[]] * n
        def bfs(node):
            que = deque([node])
            path = []
            visited = set()
            while que:
                n = que.popleft()
                visited.add(n)
                if n in graph:
                    for nbr in graph[n]:   
                        if nbr in graph and nbr not in visited:
                            visited.add(nbr)
                            path.append(nbr)
                            que.append(nbr)
                        path.append(nbr)
            return path

        for node in range(n):
            if node in graph: 
                ans[node] = sorted(list(set(bfs(node))))
        return ans

     