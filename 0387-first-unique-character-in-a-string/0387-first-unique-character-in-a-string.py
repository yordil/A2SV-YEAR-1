class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = [0] * 26

        for i in range(len(s)):
            index = 97 - ord(s[i])

            count[index] +=1
        
        for i in range(len(s)):
            index = 97 - ord(s[i])

            if count[index] == 1:
                return i
        
        return -1

