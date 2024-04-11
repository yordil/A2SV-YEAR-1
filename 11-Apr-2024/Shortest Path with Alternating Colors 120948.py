# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        graph = [[[], []] for _ in range(n)] 
        for a, b in redEdges:
            graph[a][0].append(b)
        for a, b in blueEdges:
            graph[a][1].append(b)
        
        que = deque([(0, 0) , (0 , 1)])
        visited = set([(0, 0) , (0 , 1)]) 
        ans = [-1] * n
        distance = 0
        while que:
            for i in range(len(que)):
                node , color = que.popleft()
                if ans[node] == -1:
                    ans[node] = distance
                another = 1-color
            
                for neighbour in graph[node][another]:
                    if (neighbour , another) not in visited:
                        visited.add((neighbour , another))
                        que.append((neighbour , another))

            distance +=1
        return ans 










        # graph = [[[], []] for _ in range(n)] 
        # for a, b in redEdges:
        #     graph[a][0].append(b)
        # for a, b in blueEdges:
        #     graph[a][1].append(b)
        
        # print(graph)

       
