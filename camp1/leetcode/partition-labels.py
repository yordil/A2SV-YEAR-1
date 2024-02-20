class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {}
        Sum = 0
        for i in range(len(s)):
            lastindex[s[i]] = i
        ans= []
        maxx = 0
        size = 0
        for i in range(len(s)):
            maxx = max(lastindex[s[i]] , maxx)
            size +=1
            if i == maxx:
                ans.append(size)
                size = 0
        return ans





