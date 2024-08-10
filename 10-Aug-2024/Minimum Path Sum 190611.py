# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n , m =  len(grid) , len(grid[0])
        prev = [0] * m 
        for i in range(n):
            cur = [0] * m
            for j in range(m):
                if i== 0 and j == 0 :
                    cur[j] = grid[i][j]
                else:
                    up = grid[i][j]

                    if i > 0 :
                        up += prev[j]
                    else:
                        up = float("inf")
                    
                    left = grid[i][j]

                    if j >  0 :
                        left += cur[j-1]
                    else:
                        left = float("inf")

                    cur[j]  = min(up , left)
            prev = cur
        
        return prev[m-1]
