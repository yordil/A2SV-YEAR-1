# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        outdegree = [0] * n
        
       
        for i in range(n):
            for j in graph[i]:
                reverse_graph[j].append(i)
            outdegree[i] = len(graph[i])
        
        queue = deque([i for i in range(n) if outdegree[i] == 0])
        safe_nodes = []
        
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for prev in reverse_graph[node]:
                outdegree[prev] -= 1
                if outdegree[prev] == 0:
                    queue.append(prev)
        
        return sorted(safe_nodes)
