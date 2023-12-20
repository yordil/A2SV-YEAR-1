class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        col = len(strs[0])
        count = 0
        for i in range(col):
            
            for j in range(len(strs)-1):
              
                if ord(strs[j][i]) > ord(strs[j+1][i]):
                    count+=1
                    break
        return count
        
        # for word in strs:
        #     l = len(word)
        #     # temp = word
        #     for j in range(l-1):
        #         if ord(word[j] ) > ord(word[j+1]):
        #             count+=1
        #             break
        # return count
                
            