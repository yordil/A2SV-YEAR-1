class Solution:
    def minChanges(self, s: str) -> int:
        
        i , j  = 0 , 1
        minChange  = 0
        while j < len(s):
            if s[i] != s[j]:
                minChange +=1
            i +=2
            j+=2
        
        return minChange
