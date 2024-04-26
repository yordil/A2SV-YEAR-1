# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
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
                if  size[parx] > size[pary]:
                    parent[pary] = parx
                    size[parx] += pary
                else:
                    parent[parx] = pary
                    size[pary] += parx
        def isConnected(x , y):
            return find(x) == find(y)
            
        querydictionary = defaultdict(int)
        for i in range(len(queries)):
            a , b , c = queries[i]
            querydictionary[(a , b)] =  i
        queries = [(queries[i][0],queries[i][1],queries[i][2],i ) for i in range(len(queries))]
        edgeList.sort(key = lambda x:x[2])
        queries.sort(key= lambda x:x[2])
        answer = [False] * len(queries)
        ptr = 0
        for i in range(len(queries)):
            dist = queries[i][2]
            while ptr < len(edgeList) and edgeList[ptr][2] < dist:
                union(edgeList[ptr][0] , edgeList[ptr][1])
                ptr +=1
            if isConnected(parent[queries[i][0]] , parent[queries[i][1]] ):
                index  =queries[i][3]
                answer[index]  = True
           
         

        return answer
