class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)

        for i in range(len(edges)):
            a , b  = edges[i]

            graph[a].append((b , succProb[i]))
            graph[b].append((a , succProb[i]))
    

        que = [(-1.0  , start_node)]

        heapify(que)

        visited = {}
        answer = []

        while que:
            prob , node = heappop(que)
            prob = -prob
            visited[node]  = prob 
    
            if node == end_node:
                return prob 

            for nbr , succ in graph[node]:
                latestprob = prob   * succ
                if nbr not in visited:
                    heappush(que , (-latestprob , nbr))
        
        return 0.0000






