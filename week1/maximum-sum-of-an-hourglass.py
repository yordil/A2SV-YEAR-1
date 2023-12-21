class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])
        
        maxsum = 0

        for i in range(row-3+1):
            for j in range(cols-3+1):
                Sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                maxsum = max(maxsum, Sum)
            
        return maxsum
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
#        
#             Sum  = 0
#             
#                 Sum += sum(grid[i][j : j+3])
#             Sum -=(grid[i+1][i-1] + grid[i+1]
            
        
                