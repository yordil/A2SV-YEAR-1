# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        
        for a , b in richer:
            graph[b].append(a)
        ans = [0] * len(quiet)


        def bfs(node):
            que = deque([node])
            minn = ( float("inf") , (float("inf")))
            visited = set([node])
            while que:
                n = que.popleft()
                minn = min(minn , (quiet[n] , n))
                if n in graph:
                    for nbr in graph[n]:
                        if nbr not in visited:
                            que.append(nbr)
                            visited.add(nbr)
            return minn[1]

        for i in range(len(quiet)):
            if i in graph:
                ans[i] = bfs(i)
            else:
                ans[i] = i
       
        return ans