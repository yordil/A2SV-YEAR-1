class Solution:
    def longestValidParentheses(self, s: str) -> int:


        stack = []


        
        myhash = defaultdict(int)


        stack = []
        answer = 0
        curr = 0
        for i in range(len(s)):
            
            if s[i] == "(":
                stack.append(i)

            if not stack and s[i] ==")":
                curr = 0

            if stack and s[i] == ")":
                poped  = stack.pop()
                curr = (i - poped)  + 1  + myhash[poped - 1]
                myhash[i] = curr
                print()
            answer=  max(answer , curr)

        print(myhash)
        
        return answer

    

            
        
    