class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    
        ls = sentence.split()
    
        for i in range(len(ls)):
            currlen = len(ls[i])
            if currlen >= len(searchWord):
                if ls[i][:len(searchWord)] == searchWord:
                    return i+1
        
        return -1