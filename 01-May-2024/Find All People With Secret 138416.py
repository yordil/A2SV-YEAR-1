# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], fp: int) -> List[int]: 
        meetings.sort(key= lambda x:x[2])
        parent = {i: i for i in range(n)}
        size = {i: 0 for i in range(n)}
        def find(x):
            while x != parent[x]:
                x = parent[x]
                parent[x] = parent[parent[x]]
            return x
        def union(x , y):
            parx = find(x)
            pary = find(y)
            if parx != pary:
                if size[parx] > size[pary]:
                    parent[pary] = parx
                    size[parx] += size[pary]
                else:
                    parent[parx] = pary
                    size[pary] += size[parx]
        def isConnected(x , y):
            return find(x) == find(y)

        answer = set([0 , fp])
        time = 0
        flag  = True
        visited = set()
        union(0 , fp)
        same = {}
        
        for a , b , c in meetings:
            if c not in same:
                same[c] = defaultdict(list) 
            same[c][a].append(b)
            same[c][b].append(a)

        def dfs(node , graph):
            stack = [[node , graph]]
            answer.add(node)
            seen.add(node)
            while stack:
                N , G = stack.pop()
                for nbr in G:
                    if nbr not in seen:
                        stack.append([nbr , same[time][nbr]])
                        answer.add(nbr)
                        seen.add(nbr)

        answer = set([0 , fp])
        for time in sorted(same.keys()):
            seen = set()
            for val in same[time]:
                if val in answer:
                    dfs(val , same[time][val])


        return list(answer)
                    
      