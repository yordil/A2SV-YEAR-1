class Solution:
    def myAtoi(self, s: str) -> int:
       
        INT_MAX = pow(2 , 31)  - 1
        INT_MIN = - pow(2 , 31)

        N = len(s)

        i = 0

        while i < N and s[i] == " ":
            i+=1

        if i == N:
            return 0
        
        sign  = -1 if s[i] == "-" else 1

        result = 0

        if s[i] in ['+' , '-']:
            i+=1

        for char in s[i:]:
            if not char.isdigit():
                break
            
            result = result * 10 + int(char)

            if result > INT_MAX:
                
                return INT_MAX if sign > 0 else INT_MIN 

            
        # ans  = max(INT_MIN ,  min(sign * result , INT_MAX))
        print(result)
        return result * sign
        
        


