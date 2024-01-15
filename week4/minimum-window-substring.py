from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        hasht = Counter(t)
        hashs = {}
        minwindow = float("inf")
        l = 0
        r = 0
        ll, rr = -1, -1
        
        while r < len(s):
            hashs[s[r]] = hashs.get(s[r], 0) + 1

            while all(hashs.get(key, 0) >= value for key, value in hasht.items()):
                if r - l + 1 < minwindow:
                    minwindow = r - l + 1
                    ll = l
                    rr = r
                hashs[s[l]] -= 1
                l += 1

            r += 1
        

        return s[ll:rr + 1] if ll !=-1 else ""
