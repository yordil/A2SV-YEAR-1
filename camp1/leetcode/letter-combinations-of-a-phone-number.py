class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        myhash = {
            "2" : ["a" , 'b' , 'c'] ,
            "3" : ["d" , 'e' , 'f'] ,
            "4" : ["g" , 'h' , 'i'] ,
            "5" : ["j" , 'k' , 'l'] ,
            "6" : ["m" , 'n' , 'o'] ,
            "7" : ["p" , 'q' , 'r' , 's'] ,
            "8" : [ "t" , "u" , 'v'] , 
            "9" : ['w' , 'x' , 'y' , 'z']
        }
        ans = []
        N = len(digits)
        def backtrack(i , combo):
            nonlocal N
            if len(combo) == N:
                ans.append("".join(combo.copy()))
                return 
            
            for val in myhash[digits[i]]:
                combo.append(val)
                backtrack(i+1 , combo)
                combo.pop()


        backtrack(0 , [])

        return ans if digits else []