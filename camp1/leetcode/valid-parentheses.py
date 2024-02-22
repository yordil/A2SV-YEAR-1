class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        Hash = { 
                "]" : "[" ,
                "}" : "{" ,
                ")" : "("
        
        }

        for par in s:
            if par in Hash:
                if stack and stack[-1] == Hash[par]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(par)

        return True if not stack else False