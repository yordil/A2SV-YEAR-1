class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack  = []

        for i in range(len(s)):

            if not stack:
                stack.append([s[i] , 1])
            
            else:
                if stack[-1][0] == s[i] and k-1 == stack[-1][1]:
                    copyk = k-1
                    while copyk:
                        stack.pop()
                        copyk-=1
                else:
                    if stack[-1][0] == s[i]:
                        stack.append([s[i] ,stack[-1][1] + 1])
                        continue
                    stack.append([s[i] , 1])
                    
        
        return "".join(row[0] for row in stack)