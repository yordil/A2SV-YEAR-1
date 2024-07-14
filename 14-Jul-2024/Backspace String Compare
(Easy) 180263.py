# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        copys = []
        copyt = []
        
        for i in range(len(s)):
            
            if s[i] == "#":
                if not copys:
                    continue
                else:
                    copys.pop()
                
            else: copys.append(s[i])
        
        for i in range(len(t)):
            
            if t[i] == "#":
                if  not copyt:
                    continue  
                else:
                    copyt.pop()
                
            else: copyt.append(t[i])
                
        return "".join(copyt) == "".join(copys)
                
                