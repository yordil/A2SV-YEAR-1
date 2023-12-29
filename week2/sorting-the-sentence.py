class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        rev = [0] * len(arr)
        ans = [0] * len(arr)
        for i in range(len(arr)):
            rev[i] = arr[i][::-1]
        
        rev.sort()

        for i in range(len(rev)):
            temp = rev[i]
            ans[i] = temp[1:][::-1]
        
        return " ".join(ans)
        
        
        