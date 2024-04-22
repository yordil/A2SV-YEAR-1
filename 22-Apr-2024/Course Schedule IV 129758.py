# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, num: int, prer: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for _from , to in prer:
            graph[to].append(_from)
        ans = [False] * len(queries)
        def bfs(node):
            que = deque([node])
            visited = set()
            while que:
                n = que.popleft()
                if n in graph:
                    for nbr in graph[n]:   
                        if nbr in graph and nbr not in visited:
                            que.append(nbr)
                        visited.add(nbr)        
            return list(visited)
        i = 0
        dependencylist = defaultdict(list)
        for node in range(num):
            if node in graph: 
                dependency = bfs(node)
                dependencylist[node].extend(dependency)

        i = 0
        for a, b in queries:
            if b in dependencylist and a in dependencylist[b] :
                ans[i] = True
            i+=1

        return ans

     