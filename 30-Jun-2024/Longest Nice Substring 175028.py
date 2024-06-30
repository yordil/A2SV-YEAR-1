# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        myset = set(s)
        for i in range(len(s)):
            if s[i].lower() not in myset or s[i].upper() not in myset:
                lns1 = self.longestNiceSubstring(s[:i])
                lns2 = self.longestNiceSubstring(s[i+1:])

                return max(lns1, lns2, key=len)

        return s