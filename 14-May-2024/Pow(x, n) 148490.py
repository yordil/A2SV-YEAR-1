# Problem: Pow(x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        else:
            temp = self.myPow(x , n//2)
            return temp * temp if n %2 == 0 else x * temp * temp

        # p = abs(n)
        # ans = 1.0

        # while p > 0:
        #     if p % 2 == 1:
        #         ans *= x
        #     x *= x
        #     p //= 2

        # if n < 0:
        #     return 1.0 / ans

        # return ans