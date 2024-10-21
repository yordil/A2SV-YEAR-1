# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float("inf")] * (n)
        dist[src] = 0
        for i in range(k+1):
            curr = dist[:]

            for u , v , cost in flights:
                if dist[u] + cost < curr[v]:
                    curr[v] = dist[u] + cost
            dist = curr[:]
       
        return dist[dst] if dist[dst] != float("inf") else -1






        # que = [(0 , src , 0)]
        # graph = defaultdict(list)

        # for a , b ,c in flights:
        #     graph[a].append((b , c))

        # visited = {}
        # visited[src] = 0
        # ans = float("inf")
        # while que:

        #     distance  , node , stops = heappop(que)
        #     print(node , distance , stops  , "**")
            
        #     if node == dst and stops <= k + 1:
        #         print(distance)
        #         ans = min(ans , distance)
        #     if stops <= k:
        #         for nbr , cost in graph[node]:
        #             if nbr not in visited or visited[nbr] > stops:
        #                 heappush(que , (distance + cost , nbr , stops + 1))
                        
            

        # return -1 if ans == float("inf") else ans
                    