# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n , m = len(obstacleGrid) , len(obstacleGrid[0])
        if obstacleGrid[n-1][m-1] == 1 or obstacleGrid[0][0] == 1:
                return 0
        else:
            prev = [0]  * m
            aa = obstacleGrid[0]
            for i in range(len(aa)):
                if aa[i] == 1:
                    break
                prev[i] = 1
        # print(prev)
        for i in range(1 , n):
            curr = [0] * m
            if obstacleGrid[i][0] != 1:
                curr[0] = prev[0]
            # print(curr , prev)
            for j in range(1 , m):
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0 
                    continue
                if curr[j-1] == 0:
                    curr[j] = prev[j] 
                    continue
                
                curr[j] = prev[j] + curr[j-1]
            prev = curr
        print(prev)
        return prev[-1]