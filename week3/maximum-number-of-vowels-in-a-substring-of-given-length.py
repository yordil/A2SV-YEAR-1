class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        arr = [ 'a' , 'e' , 'i' , 'o'   , 'u']
        best = 0
        count = 0
        
        for i in s[:k]:
            if i in arr:
                count+=1
            if count > best:
                best = count
                    
        for i in range(k , len(s)):
            if s[i-k] in arr:
                count -=1
            if s[i] in arr:
                count +=1
            best = max(best, count)
            
        return best
        
        
        