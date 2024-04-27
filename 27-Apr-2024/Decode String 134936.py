# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
     
        idx  = 0
        
        def decode(s , idx , num):
            ans = []
            i = idx
            while i < len(s) and s[i] != "]":
                if s[i].isdigit():
                    numidx = i
                    while len(s) > i and s[i].isdigit() :
                        i +=1
                    lastidx , val = decode(s , i , int(s[numidx:i]))
                    i = lastidx + 1
                    ans.extend(val)
                elif s[i] != "[":
                    ans.append(s[i])
                    i+=1
                else:
                    i+=1
            ans *= num

            return i , ans
        
        _  , ans = decode(s , 0 , 1)
        return "".join(ans)

                
                    