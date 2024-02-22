class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        ans = 0
        ansstack = []
        stack = []
    
        for par in s:
            if par == "(":
                stack.append(par)
                
            else:
                if stack[-1] == "(":
                    stack[-1] = 1
                elif stack[-1] != "(":
                    temp = 0
                    while stack and stack[-1] != "(":
                        temp+=stack.pop()
                    stack[-1]=temp*2
        return sum(stack)











   
        # ans = 0
        # ansstack = []
        # stack = []
        # flag = False
        # for par in s:
        #     if par == "(":
        #         stack.append(par)
        #         flag = False
        #     else:
        #         # stack.pop()
        #         # if ans == 0:
        #         #     ans +=1 
        #         #     ansstack.append(1)
        #         # elif len(ansstack) >
        #         # elif flag and len(ansstack) >= 2:
        #         #     ansstack[-1] += ansstack[-2]
        #         # elif flag:
        #         #     ans *=2
        #         #     ansstack[-1] *=2
        #         else:
        #             ansstack.append(1)

        #         flag = True

        # return ansstack[-1]