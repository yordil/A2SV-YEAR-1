class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        length = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                
                l+=1
                
            hashset.add(s[r])
            
            length = max(length , len(hashset))
        return length
                
                
            
            
          
        