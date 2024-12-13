class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #  length_of_the_word
        def check_remain(p , ans,  word):

            while p < len(word):
                ans.append(word[p])
                p+=1

        l1 , l2 = len(word1) , len(word2)

        ans = []
        p1 , p2 = 0 , 0 
        
        while p1 < l1 and p2 < l2:
            ans.append(word1[p1])
            ans.append(word2[p2])
            p1+=1
            p2 +=1
        
        check_remain(p1 , ans , word1)
        check_remain(p2 , ans , word2)


        return "".join(ans) 





