class Solution:
    def isMatch(self, s: str, p: str) -> bool:
       

        star = -1
        backposition = 0

        i , j  = 0  ,  0  


        while i < len(s):

            if j < len(p) and  (s[i] == p[j] or p[j] == "?"):
                i+=1
                j+=1
            elif j < len(p) and p[j] == "*":
                star = j
                backposition = i 
                j+=1
            elif star != -1:
                i = backposition + 1
                j = star + 1
                backposition += 1


            else:
                return False

        for i in range(j , len(p)):
            if p[i] != "*":
                return False
        
        return True
    
