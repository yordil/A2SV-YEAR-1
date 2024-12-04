class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False

        l , r = 0 , 0
        while l < len(str1) and r  < len(str2):
            if str1[l] == str2[r]:
                l +=1
                r +=1
            elif str1[l] != "z" and (ord(str1[l])) + 1 == ord(str2[r]):
                l+=1
                r+=1
            elif str1[l] == "z" and str2[r] == "a":
                l+=1
                r+=1
            else:
                l +=1
        print(l , r)
        return r == len(str2)
        