class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        

        def inbound(row , col):
            return 0<=row < len(grid) and 0<=col < len(grid[0])
        # Define FourDirection list
        FourDirection = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        seen= defaultdict(lambda: float("inf"))

        heap = [(0 , 0 , 0)]

        seen[(0 , 0)] = 0

        while heap:

            dist , row , col = heappop(heap)

            if row == len(grid) - 1  and col == len(grid[0]) - 1:
                return dist

            for x , y in FourDirection:
                nr , nc = x+row , y+col

                if inbound(nr , nc) and  grid[nr][nc] + dist < seen[(nr , nc)]:
                    seen[(nr , nc)] = grid[nr][nc] + dist
                    heappush(heap , (grid[nr][nc] + dist , nr , nc))
        
        








    



