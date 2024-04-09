# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(1 ,0) , (-1, 0) , (0, 1) , (0, -1)]
        que = deque()
        def inbound(row , col):
            print(5)
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        def bfs():
            nonlocal fresh
            count = 0
            minutes = -1
            visited = set()
            while que:
                minutes +=1
                for i in range(len(que)):
                    start , end = que.popleft()
                    visited.add((start , end))
                   
                    for nc , nr in direction:
                        newrow , newcol = nr+start , nc + end
                        if inbound(newrow , newcol) and grid[newrow][newcol] == 1:
                            fresh -=1
                            grid[newrow][newcol] = 2
                            que.append((newrow , newcol))
            # print(minutes , fresh)
            return minutes if fresh == 0 else -1
                    
                    
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    que.append((i, j))
                if grid[i][j] == 1:
                    fresh +=1
        if fresh == 0:
            return 0
        else:
            return bfs()
        
        