class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        que = [(0 , k)]

        graph = defaultdict(list)

        for a , b , c in times:
            graph[a].append((b , c))

        heapify(que)
        visited = set()
        while que:

            distance , node = heappop(que)
            visited.add(node)
            print(distance)
            if len(visited) == n:
                return distance
            for nbr , dist in graph[node]:
                if nbr not in visited:
                    heappush(que , (distance + dist , nbr))

        return  -1

