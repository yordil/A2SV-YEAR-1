class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        i, n = 0, len(s)
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            count = j - i
            count %= k
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] = (stack[-1][1] + count) % k
                if stack[-1][1] == 0:
                    stack.pop()
            elif count:
                stack.append([s[i], count])
            i = j

        ans = [c * v for c, v in stack]
        return "".join(ans)







        # stack  = []

        # for i in range(len(s)):

        #     if not stack:
        #         stack.append([s[i] , 1])
            
        #     else:
        #         if stack[-1][0] == s[i] and k-1 == stack[-1][1]:
        #             copyk = k-1
        #             while copyk:
        #                 stack.pop()
        #                 copyk-=1
        #         else:
        #             if stack[-1][0] == s[i]:
        #                 stack.append([s[i] ,stack[-1][1] + 1])
        #                 continue
        #             stack.append([s[i] , 1])
                    
        
        # return "".join(row[0] for row in stack)