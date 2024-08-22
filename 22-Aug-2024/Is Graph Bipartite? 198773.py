# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
    
        color = [-1 for i in range(len(graph))]
        print(color)
        color[0] = 0

        stack = [(0 , 0)]
        visited = set()
        for i in range(len(graph)):
            if i not in visited:
                stack.append((i , 0))
                while stack:
                    node , currcolor = stack.pop()
                    visited.add(node)
                    for nbr in graph[node]:
                        if color[nbr] == -1:
                            color[nbr] = 1 - currcolor  
                            stack.append((nbr , 1-currcolor))
                        elif color[nbr] == currcolor:
                            return False


        return True





