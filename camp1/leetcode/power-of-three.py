class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def helper(n):


            if n == 1:
                return True
            elif n < 1:
                return False

            return helper(n/3)

        return helper(n)
