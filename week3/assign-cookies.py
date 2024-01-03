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
                j+=1
            
        return  count


