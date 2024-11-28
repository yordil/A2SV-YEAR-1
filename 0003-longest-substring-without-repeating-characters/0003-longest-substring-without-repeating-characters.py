class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charhold = [-1] * 128
        l , answer = 0  ,  0
        for idx ,  char in enumerate(s):
            if charhold[ord(char)] >= l:
                l = charhold[ord(char)] +  1
            else:
                answer = max(answer , idx - l  +1)

            charhold[ord(char)]  = idx

        return answer        
        
        # hashset = set()
        # l = 0
        # length = 0
        # for r in range(len(s)):
        #     while s[r] in hashset:
        #         hashset.remove(s[l])
                
        #         l+=1
                
        #     hashset.add(s[r])
            
        #     length = max(length , len(hashset))
        # return length
                
                
            
            
          
        