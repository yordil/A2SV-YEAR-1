# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prev = [1] * n

        for i in range(1 , m):
            curr = [0] * n 
            curr[0] = 1
            for j in range(1 , n):
                 curr[j] = prev[j] + curr[j-1]
            prev = curr
        
        return prev[-1]