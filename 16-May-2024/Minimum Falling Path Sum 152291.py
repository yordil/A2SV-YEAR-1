# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        N = len(matrix)
        def inbound(c):
            return 0 <= c < len(matrix)

        for i in range(1 , N):
            for j in range(N):
                minn = float(inf)
                if inbound(j):
                    minn = min(minn , matrix[i-1][j])
                if inbound(j+1):
                    minn = min(minn , matrix[i-1][j+1])
                if inbound(j-1):
                    minn = min(minn , matrix[i-1][j-1])
                
                matrix[i][j] += minn
        return min(matrix[N-1])

                    