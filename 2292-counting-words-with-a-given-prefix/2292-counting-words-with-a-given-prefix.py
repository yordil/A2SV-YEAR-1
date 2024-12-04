class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count =  0
        for i in range(len(words)):
            currlen = len(words[i])
            if currlen >= len(pref):
                if words[i][:len(pref)] == pref:
                    count +=1 
        
        return count 