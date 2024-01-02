class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        Str = ""
        
        for i in s:
            if i.isalnum():
                Str +=i.lower()
            
        #  return Str == Str[::-1] easier way to do:
        
        l , r  = 0 , len(Str)-1
        
        while l < r:
            
            if Str[l] != Str[r]:
                return False
            
            l+=1
            r-=1
            
        return True
            