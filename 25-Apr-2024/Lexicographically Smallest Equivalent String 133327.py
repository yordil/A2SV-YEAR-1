# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, base: str) -> str:

        parent = {chr(i):chr(i) for i in range(97 , 124)}
        def find(x):
            while x != parent[x]:
                x = parent[parent[x]]
            return x

        def union(a , b):
            par1 = find(a)
            par2 = find(b)

            if par1 != par2:
                if par1 < par2:
                    parent[par2] = par1
                else:
                    parent[par1] = par2
            
        for i in range(len(s1)):
            union(s1[i] , s2[i])
        
        ans = ""
        for b  in base:
            ans += find(b)
        return ans

        
