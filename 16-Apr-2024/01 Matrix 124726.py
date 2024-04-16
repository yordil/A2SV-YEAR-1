# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        direction = [ (1 ,0) , (-1 ,0) , (0 ,1) , (0 ,-1)]
        def inbound(r , c):
            return 0 <= r < len(mat) and 0 <= c < len(mat[0])
        arr = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    arr.append((i , j))
                else:
                    mat[i][j] = "."
        
        for a , b in arr:
            for x , y in direction:

                nr = a + x
                nc  = b + y
                if inbound(nr , nc) and mat[nr][nc] == ".":
                    mat[nr][nc] = mat[a][b] + 1
                    arr.append((nr , nc))
               

        return mat








        # ans = []
        # def bfs():
        #     que = deque([(0 , 0)])
        #     visited = set()

        #     # while que:
        #     #     row , col  = que.pop()
        #     #     for r , c in direction:
        #     #         nr = r + row
        #     #         nc = c + col
        #     #         if inbound(nr , nc) and 
                