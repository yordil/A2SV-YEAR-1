# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        swapcount = 0

        left = 0 
        right = len(s) - 1
        s = list(s)
        zeros = s.count("0")
        ones = s.count("1")
        while left < right:
            if s[left] == "1" and s[right] == "0":
                swapcount += right - left 
                right -=1
                left +=1
                continue
            if s[left] == "0":
                left+=1
            if s[right] == "1":
                right -=1
            
            if left == zeros:
                break

        return swapcount