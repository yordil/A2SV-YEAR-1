# Problem: Ugly Number - https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        prime  = [2 , 3 , 5 , 7]
        j = 0
        while n > 1:
            if j == 3:
                return False
            if n % prime[j] == 0:
                n /= prime[j]
            else:
                j+=1

        return True
            