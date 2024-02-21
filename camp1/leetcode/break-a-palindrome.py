class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1 and len(set(palindrome)) == 1:
            return ""
        else:
            ss = list(palindrome)

            left , right =  0 , len(ss) - 1 

            while left < right:
                if ss[left] == ss[right] == "a":
                    left +=1
                    right -=1
                    if left >= right:
                        ss[-1] = "b"
                    continue
                else:
                    ss[left] = "a"
                    break
                left +=1
                right -=1
            
            return "".join(ss)
