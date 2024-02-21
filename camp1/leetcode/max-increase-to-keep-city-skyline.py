class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        inversed = list(zip(*grid))
        print(inversed)
        
        
        for i in range(len(grid)):
            maxrow = max(grid[i])
            for j in range(len(grid[0])):
                minOfthetwo = min(maxrow , max(inversed[j]))

                ans += (minOfthetwo - grid[i][j])

        return ans 
