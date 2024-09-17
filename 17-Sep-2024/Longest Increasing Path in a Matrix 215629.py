# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        
        rows, cols = len(matrix), len(matrix[0])
        memo = [[-1] * cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols
        def dfs(r, c):
            if memo[r][c] != -1:
                return memo[r][c]
            
            maxx = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inbound(nr , nc) and matrix[nr][nc] > matrix[r][c]:
                    maxx = max(maxx, 1 + dfs(nr, nc))
            
            memo[r][c] = maxx
            return maxx
        
        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))
        
        return ans