# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        empty = ""
        
        sptr , tptr = 0 , 0
        
        for i in range(len(t)):
            if sptr == len(s):
                break
            
            if t[i] == s[sptr]:
                sptr+=1
                
                
        return True if sptr == len(s) else False