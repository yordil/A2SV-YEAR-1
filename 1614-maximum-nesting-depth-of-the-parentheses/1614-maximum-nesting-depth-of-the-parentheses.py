class Solution:
    def maxDepth(self, s: str) -> int:
        opencount = 0

        stack = []
        
        ans = 0
        for i in range(len(s)):
            if s[i] == "(":
                opencount +=1
                stack.append("(")
            elif s[i] == ")":
                stack.pop()
                opencount -=1
            ans = max(ans , opencount)
            
        return ans 
                
