# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
         
        answer  = 0
        direction = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]
        visited = set()
        def inbound(r , c):
            return 0<=r < len(grid) and 0 <=c < len(grid[0])
        def bfs(i , j):

            queue = deque()
            queue.append((i , j))
            counter = 1
            visited.add((i ,j))

            while queue:
                row , col = queue.popleft()

                for x , y in direction :
                    newrow , newcol = row + x , col + y

                    if inbound(newrow , newcol) and (newrow , newcol) not in visited and grid[newrow][newcol] == 1:
                        queue.append((newrow , newcol))
                        visited.add((newrow , newcol))
                        counter +=1
            return counter


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i , j ) not in visited and grid[i][j] == 1:
                    answer = max(answer , bfs(i ,j))

        return answer

