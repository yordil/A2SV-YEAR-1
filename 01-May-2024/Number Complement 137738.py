# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        ans = ""
        while num:
            ans += str(1-num%2)
            num = num // 2
        return int(ans[::-1] , 2)