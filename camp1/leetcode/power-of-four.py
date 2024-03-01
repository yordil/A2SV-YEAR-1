class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def helper(n):


            if n == 1:
                return True
            elif n < 1:
                return False

            return helper(n/4)

        return helper(n)
