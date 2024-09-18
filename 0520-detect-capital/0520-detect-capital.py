class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        l , r = 0 , 1
        
        if ord(word[l]) > ord("Z"):
            for i in range(1 , len(word)):
                if ord(word[i]) < ord("a"):
                    return False
            return True
        else:
            if ord(word[r]) > ord("Z"):
                for i in range(1 , len(word)):
                    if ord(word[i]) < ord("a"):
                        return False
                return True
            else:
                for i in range(1 , len(word)):
                    if ord(word[i]) >= ord("a"):
                        return False
        
        return True




        