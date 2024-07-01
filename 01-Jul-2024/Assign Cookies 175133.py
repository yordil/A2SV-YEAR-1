# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        ans = 0
        j = 0
        for i in range(len(g)):
            while j < len(s) and g[i] > s[j]:
                j+=1
            if j < len(s):
                count+=1
                j+=1 # because the cookie in that index is taken by g[i]'s person
            
        return  count

