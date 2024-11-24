class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x and x % 10 == 0):
            return False

        reverse = 0

        while reverse < x:
            
            reverse = reverse*10 + x % 10

            x //= 10
        
        return x in (reverse , reverse// 10)

