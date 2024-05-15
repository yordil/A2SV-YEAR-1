# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        memo = {}
         
        @cache
        def dp(i , j ):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                x = 1 + dp(i+1 , j + 1)
            else:
                x = max(dp(i+1 , j ) , dp(i , j+1 ) )
            
            return x

        
        return (dp(0 , 0))
        

            
            


        
