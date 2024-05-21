# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def dp(idx , aa):
            if idx >= len(triangle):
                return 0
            take = dp(idx+1 , aa+1 )+ triangle[idx][aa]
            leave  = dp(idx+1 , aa)+  triangle[idx][aa]

            return min(take , leave)


        return dp(0 , 0) 
