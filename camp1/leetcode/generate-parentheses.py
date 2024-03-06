class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      
        # print(default)
        path = []
        
        ans = set()
        def backtrack( path , open , close):
            if open == 0 and close == 0:
                a = path.copy()
                a = tuple(a)
                
                print(55)
                ans.add("".join(a))
                return
            
            if open > 0:
                path.append("(")
                backtrack(path , open - 1 , close)
                path.pop()
            if close > 0 and open < close:
                path.append(")")
                backtrack(path ,open , close-1)
                path.pop()


                  

        backtrack(path , n , n)

        return list(ans)












        
            # for i in range(2*n -1):
            #     if path.count("(") < open:
            #         path.append("(")
            #         backtrack(open -1 , close)
            #         a = path.pop()
            #         if a == "(":
            #             open +=1
            #         else:
            #             close = close + 1

            #     if path.count(")") < close and path.count("(") > path.count(")"):
            #         path.append(")")
            #         backtrack(open , close-1)
            #         a = path.pop()
            #         if a == "(":
            #             open +=1
            #         else:
            #             close = close + 1