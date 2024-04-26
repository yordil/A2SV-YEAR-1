# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {i:i for i in range(len(stones))}
        size = {i:0 for i in range(len(stones))}

        def find(x):
            while x != parent[x]:
                x = parent[x]
            
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

        visited = defaultdict(int)
        visited[(stones[0][0] , stones[0][1])] = 0
       
        for i in range(1 , len(stones)):
            a , b = stones[i]
            for key , val in visited.items():
                if key[0] == a or key[1] == b :
                    union(val , i)
                   

            visited[(stones[i][0] , stones[i][1])] = i

        count = 0

        for i in range(len(stones)):
            if find(i) != i:
                count +=1

        return count
