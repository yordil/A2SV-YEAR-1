class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * len(s)

        for start , end , dirn in shifts:
            if dirn:
                prefix[start] +=1
                if end < n-1:
                    prefix[end+1] -=1
            else:
                prefix[start] -=1
                if end < n-1:
                    prefix[end+1] +=1
            
        prefix = list(accumulate(prefix))
        print(prefix)
        
        
        ans = []
        for i in range(n):
            shifted_char = chr((ord(s[i]) - ord('a') + prefix[i]) % 26 + ord('a'))
            ans.append(shifted_char)

        return "".join(ans)


     


            