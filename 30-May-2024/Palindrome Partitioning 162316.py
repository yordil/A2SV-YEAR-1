# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        an  = []
        temp = []
        
        def backtrack(start):
            if start >= len(s):
                an.append(temp.copy())
                return 
         
            for i in range(start , len(s)):

                if s[start:i+1] == s[start:i+1][::-1]:
                    temp.append( s[start:i+1])
                    backtrack(i+1)
                    temp.pop()
                
        
        backtrack(0)
        
        return an



                