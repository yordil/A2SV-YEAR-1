class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        ans = ""
        acount = 0
        bcount  = 0
        while a > 0 or b > 0:
            if (a  > b and acount < 2) or bcount == 2:
                ans += "a"
                acount +=1
                bcount = 0
                a-=1
            elif (b and bcount < 2) or acount == 2:
                ans+= "b"
                acount  = 0
                bcount += 1 
                b-=1
            
        return ans
        
            