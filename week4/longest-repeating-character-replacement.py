class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapp = {}
        l = 0
        length = 0        
        for r in range(len(s)):
            mapp[s[r]] = 1 + mapp.get(s[r] , 0) 
             
            while (r-l+1) - max(mapp.values()) > k:
                mapp[s[l]] -=1
                l +=1  
            length = max(length , r-l+1)
        return length