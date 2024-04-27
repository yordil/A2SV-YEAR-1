# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        directions = [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]

        def inbound(row , col):
            return 0 <= row < len(grid) and 0<= col < len(grid[0])
        
        visited = set()
        def bfs(startrow , startcol):
            que = deque()
            que.append([startrow , startcol])
            visited.add((startrow , startcol))
            eachsum = grid[startrow][startcol]
            
            while que:
                row , col = que.popleft()

                for x , y in directions:
                    new_row , new_col = x+ row , y + col

                    if inbound(new_row , new_col) and grid[new_row][new_col] \
                    and (new_row , new_col) not in visited:
                        eachsum += grid[new_row][new_col]
                        visited.add((new_row , new_col))
                        que.append([new_row , new_col])
            return eachsum
        maximum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i , j) not in visited and grid[i][j]:
                    maximum  =  max(maximum , bfs(i , j))

        return maximum 
        
            