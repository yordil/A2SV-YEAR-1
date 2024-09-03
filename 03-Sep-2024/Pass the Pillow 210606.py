# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        if time < n:
            return 1+time

        quo =  time // (n - 1)
        remain = time % (n-1)
        
        if quo % 2 or quo == 0:
            
            return n - remain
        else:
            return 1 + remain

