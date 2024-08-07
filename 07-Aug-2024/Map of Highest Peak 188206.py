# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        direction = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]
        row , col = len(isWater) , len(isWater[0])

        def inbound(r : int , c : int) -> bool:
            return 0 <= r < row and 0 <= c < col

        answer = [[0] * col for _  in range(row)]
        visited = set()

        myque = deque()
        def bfs()->List[List[int]]:
           
            while myque:
                r , c , val = myque.popleft()
                
                for x , y in direction:
                    nr , nc  = x+ r , c+ y
                    if (nr , nc) not in visited and \
                     inbound(nr  , nc) and isWater[nr][nc] == 0:
                     visited.add((nr , nc))
                     myque.append((nr , nc , val + 1))
                answer[r][c] = val
        
        for i in range(row):
            for j in range(col):
                if isWater[i][j]:
                    myque.append((i , j , 0))

        bfs()
        return answer
