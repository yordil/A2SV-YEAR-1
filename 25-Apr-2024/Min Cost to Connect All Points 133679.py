# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        parent = {i:i for i in range(len(points))}
        size = {i:0 for i in range(len(points))}

        def find(x):
            while x != parent[x]:
                x = parent[parent[x]]
            
            return x

        def union(x,y):
            parentX = find(x)
            parentY = find(y)

            if parentX != parentY:
                if size[parentX] > size[parent[y]]:
                    parent[parentY] = parentX
                    size[parentX] += size[parentY]
                else:
                    parent[parentX] = parentY
                    size[parentY] += size[parentX]


        def isConnected(x , y):
            return find(x) == find(y)

        ans = 0

        edgecost = []

        for i in range(len(points)):
            for j in range(i+1  ,len(points)):
                dist  = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                val = [dist  , i , j]
                edgecost.append(val)

        edgecost.sort()


        for i in range(len(edgecost)):
            if not isConnected(edgecost[i][1] , edgecost[i][2]):
                ans += edgecost[i][0]
                union(edgecost[i][1] , edgecost[i][2])
        return ans