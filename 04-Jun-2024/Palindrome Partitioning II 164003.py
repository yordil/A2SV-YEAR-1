# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        if len(s) == 1 and s == s[::-1]:
            return 0
        
        temp  = []
        memo = {}
        maxans  = float("inf")
        
        def dp(start):
            if start >= len(s):
                return 0
            if start in memo:
                return memo[start]
            
            min_cuts = float('inf')
            for end in range(start, len(s)):
                if s[start : end+1] == s[start: end+1][::-1]:
                    min_cuts = min(min_cuts, 1 + dp(end + 1))
            
            memo[start] = min_cuts
            return min_cuts
        
        return dp(0) - 1